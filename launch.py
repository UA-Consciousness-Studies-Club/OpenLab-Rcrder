#!/usr/bin/env python3
"""One-click launcher for OpenLab Recorder (target of the desktop icon).

Auto-detects the OpenBCI dongle's serial port, opens LabRecorder, and starts the
bridge in this console window. Close the window (or Ctrl-C) to stop streaming.

    python launch.py            # board defaults to daisy (Cyton+Daisy, 16 ch)
    python launch.py cyton      # 8-channel Cyton
"""
from __future__ import annotations

import platform
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BRIDGE = HERE / "src" / "openbci_lsl_bridge.py"
VENDOR = HERE / "vendor" / "LabRecorder"

FTDI_VID = 0x0403  # OpenBCI dongle uses an FTDI USB-serial chip


def find_labrecorder() -> Path | None:
    """Locate the LabRecorder binary for the current platform.

    The labstreaminglayer/App-LabRecorder release names the binary differently
    per OS:
      - Windows:  LabRecorder.exe       (loose binary inside a folder)
      - macOS:    LabRecorder.app       (app bundle; launch via `open`)
      - Linux:    LabRecorder           (loose binary, no extension)
    """
    if not VENDOR.exists():
        return None
    system = platform.system()
    if system == "Windows":
        return next(VENDOR.rglob("LabRecorder.exe"), None)
    if system == "Darwin":
        # Find the .app bundle directly; rglob would also descend INTO it and
        # return Contents/MacOS/LabRecorder which is the inner executable
        # (still launchable, but `open` on the .app is the canonical path).
        for p in VENDOR.rglob("LabRecorder.app"):
            return p
        # Fallback: inner executable, in case extraction flattened the bundle
        return next(VENDOR.rglob("MacOS/LabRecorder"), None)
    # Linux (and any other Unix)
    for p in VENDOR.rglob("LabRecorder"):
        if p.is_file() and p.stat().st_mode & 0o111:  # executable bit set
            return p
    return None


def launch_labrecorder(path: Path) -> None:
    """Spawn LabRecorder appropriate to its binary type on this OS."""
    if platform.system() == "Darwin" and path.suffix == ".app":
        # macOS app bundle: use Launch Services via `open`. Plain Popen of
        # the .app directory does not work.
        subprocess.Popen(["open", str(path)])
    else:
        subprocess.Popen([str(path)])


LABRECORDER = find_labrecorder()


def find_dongle_port() -> str | None:
    try:
        from serial.tools import list_ports
    except ImportError:
        print("pyserial not installed — run: python install.py  (or pip install pyserial)")
        return None
    ports = list(list_ports.comports())
    for p in ports:  # prefer the FTDI dongle
        if p.vid == FTDI_VID:
            return p.device
    for p in ports:  # otherwise first USB serial device
        if "USB" in (p.description or "") or "Serial" in (p.description or ""):
            return p.device
    return ports[0].device if ports else None


def main() -> int:
    board = sys.argv[1] if len(sys.argv) > 1 else "daisy"
    port = find_dongle_port()
    if not port:
        print("No serial dongle found. Plug in the OpenBCI dongle and re-run.")
        input("Press Enter to close...")
        return 1
    print(f"OpenBCI dongle: {port}  |  board: {board}")

    if LABRECORDER:
        print(f"Opening LabRecorder: {LABRECORDER.name}")
        launch_labrecorder(LABRECORDER)
        time.sleep(1.0)
    else:
        print(f"LabRecorder not found in vendor/ for platform {platform.system()} — run: python install.py")

    print("Starting stream. In LabRecorder, click Update, check 'OpenBCI_EEG', then Start.")
    print("Close this window or press Ctrl-C to stop streaming.\n")
    return subprocess.call([sys.executable, str(BRIDGE), "--port", port, "--board", board])


if __name__ == "__main__":
    raise SystemExit(main())

# Third-party notices

OpenLab Recorder depends on, and in one module adapts, third-party open-source
software. The dependencies it downloads or installs at runtime (BrainFlow,
liblsl / pylsl, LabRecorder, pyxdf, pyserial) are obtained from their own
distributions and carry their own licenses; they are not redistributed in this
repository. See [CREDITS.md](CREDITS.md) for the full list, roles, and links.

This file reproduces the copyright and permission notices for the MIT-licensed
projects whose source was **adapted** into this repository (currently
`src/impedance_check.py`), as the MIT License requires.

---

## OpenBCI_GUI

The electrode-impedance ohms formula in `src/impedance_check.py`
(`Z = (sqrt(2) * Vrms) / I_drive - R_series`, with `I_drive = 6 nA`,
`R_series = 2200 ohms`) is adapted from OpenBCI_GUI (`DataProcessing.pde`,
`BoardCyton.pde`).

Source: https://github.com/OpenBCI/OpenBCI_GUI

```
MIT License

Copyright (c) 2018 OpenBCI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## pyOpenBCI-impedance (mikito-ogino)

The Python pattern in `src/impedance_check.py` for configuring the Cyton
lead-off command (`z CH P N Z`) and the bandpass + root-mean-square measurement
approach is adapted from pyOpenBCI-impedance.

Source: https://github.com/mikito-ogino/pyOpenBCI-impedance

```
MIT License

Copyright (c) 2025 mikito-ogino

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

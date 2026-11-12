This repository and its wheels are experimental. Please report any issue at
https://github.com/librelane/openroad-wheels/issues.

---

# OpenROAD Wheels

Unofficial pre-built binary wheels for
[OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD), also including the
full OpenROAD binary with a Tcl interpreter.

## Requirements

* Any of:
    * macOS 15 or later  (arm64)
    * GNU/Linux with Glibc 2.27 or later (x86_64 or aarch64)
* Python 3.10 or later

## Installation

```bash
pip3 install --upgrade lln-openroad
```

## Usage

```bash
openroad
# OR
python3 -c "import openroad; print(', '.join(dir(openroad)))"
```

## Caveats

* The OpenROAD Qt GUI is not supported.
* The OpenROAD binary requires a one-time extraction step which must be
  `gunzip`ped ahead of time for read-only environments.
* We cannot guarantee more than one .post version per OpenROAD version will be
  up on PyPI at the same time due to storage requirements, and as we approach
  the total storage limit, older versions may be removed.
  * For long-term reproducible environments, we recommend downloading the binary
    wheels from GitHub Releases.

## Why include the full binary?

Starting November 2026, OpenROAD has removd the CMake build system, requiring
the use of Bazel to compile OpenROAD. We have no estimate on when OpenROAD will
receive a Nix derivation that supports Bazel and thus we may choose to package
these wheels as binary derivations (those that patch pre-compiled executables to
work within the Nix environment) starting in 2027.

## Licensing

### Binaries

As the binary incorporates OpenSTA code, the binaries are distributed under the
GNU General Public License, v3, or any later version. See [COPYING](./COPYING)
for more info.

### Code

Copyright (c) 2018-2025, The OpenROAD Authors.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1.  Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.

2.  Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

3.  Neither the name of the copyright holder nor the names of its contributors
    may be used to endorse or promote products derived from this software
    without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


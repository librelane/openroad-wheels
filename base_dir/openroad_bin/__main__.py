# Copyright (c) 2026 Mohamed Gaber
# SPDX-License-Identifier: BSD-3-Clause
#
# Parts adapted from misli/python-flock, Copyright (c) 2014, Jakub Dorňák
# under the same license
import fcntl
import gzip
import os
import sys
from pathlib import Path

__here__ = Path(__file__).resolve().parent


class Flock:
    def __init__(self, fd):
        (self.fd, self.op) = (fd, fcntl.LOCK_EX)

    def __enter__(self):
        fcntl.lockf(self.fd, self.op)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        fcntl.lockf(self.fd, fcntl.LOCK_UN)

def _ensure_extracted():
    extracted = __here__ / "openroad"
    with open(__here__ / ".extraction-lock", "w") as f, Flock(f.fileno()):
        if not extracted.is_file():
            gzipped = __here__ / "openroad.gz"
            if not gzipped.is_file():
                print(
                    "Error: Compressed OpenROAD binary not found. Try reinstalling the wheel. Exiting.",
                    file=sys.stderr,
                )
                sys.exit(1)
            print(
                "Performing first-time extraction for OpenROAD binary...",
                file=sys.stderr,
            )
            with gzip.open(gzipped) as f_in, open(extracted, "wb") as f_out:
                f_out.write(f_in.read())
            os.chmod(extracted, 0o555)
    return extracted

def openroad():
    os.execlp(_ensure_extracted(), "openroad", *sys.argv[1:])

def sta():
    os.execlp(_ensure_extracted(), "sta", *sys.argv[1:])

if __name__ == "__main__":
    openroad()

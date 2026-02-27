#!/usr/bin/env python

# Note, you need to pip install python-magic to use this.

import magic
import os
import sys


def fix_with_magic(filename):
    base, ext = os.path.splitext(filename)
    if ext:
        print(f"skipping {filename}")
        return

    result = magic.from_file(filename, mime=True)
    if result.startswith("text/"):
        new_name = filename + "." + result[5:]
        if os.path.exists(new_name):
            print(f"{new_name} already exists!")
            raise SystemExit(1)
        os.rename(filename, new_name)
    else:
        print(f"Unsupported! {filename}")
        raise SystemExit(1)


if __name__ == "__main__":
    fix_with_magic(sys.argv[1])

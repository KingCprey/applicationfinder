#!/usr/bin/env python3
import applicationfinder
import os
atom_file=".desktops/atom.desktop"
if os.path.exists(atom_file):
    src=""
    with open(atom_file,'r')as inp:
        src=inp.read()
    parsed=applicationfinder.parse_desktop(src)
    print(parsed)

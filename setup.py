# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:36:15 2024

@author: Fred
"""

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="MochiSearchAndConvert",
    version="0.1",
    description="Search and convert .mochi files",
    executables=[Executable("convert_mochi_tkinter.py", base="Win32GUI")]
)

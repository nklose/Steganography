#####################################
# steganography.py version 1.0      #
# Nick Klose | nick.klose@gmail.com #
# py2exe setup script               #
#####################################

from distutils.core import setup
import py2exe, os, sys

root_dir = os.path.dirname(os.path.realpath("__file__"))
main_file = os.path.join(root_dir, "steganography.py")
exe_name = "Steganography"
incl_files = [os.path.join(root_dir, "sample.jpg"),
    os.path.join(root_dir, "README.md"),
    os.path.join(root_dir, "LICENSE")]
excl_dlls = ["libiomp5md.dll", "MSVCP60.DLL", "MSVCP90.DLL", "MSVCP100.DLL"]
windowsSettings = [{"dest_base": exe_name, "script": main_file}]
incl_packages = ["sip"]

options = {
    'py2exe': {
        "dist_dir": "bin",
        "includes": incl_packages,
        "dll_excludes": excl_dlls,
        "bundle_files": 1,
        "compressed": 2,
        "optimize": 2,
        "xref": False,
        "skip_archive": False,
        "ascii": False,
    }
}

setup(
    windows = windowsSettings,
    author = "Nick Klose",
    version = "1.0",
    description = "Nick's Image Steganography",
    name = "Nick's Image Steganography",
    options = options,
    data_files = incl_files,
    zipfile = None
)
from distutils.core import setup
from Cython.Build import cythonize
import os
os.environ['CFLAGS'] = '-O3 -Wall -std=c++17 -mavx2 -fabi-version=0 -mfma'
ext_options = {"compiler_directives": {"profile": True}, "annotate": True}
setup(ext_modules = cythonize("par_sig.pyx", ** ext_options))
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

package = Extension('ChsRX', ['ChsRX.pyx'], include_dirs=[numpy.get_include(),"/usr/local/lib/python3.10/dist-packages/numpy/_core/include/"])
setup(ext_modules=cythonize([package]))

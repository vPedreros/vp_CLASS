from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as nm
import os
import subprocess as sbp
import os.path as osp

liblist = ['class']
liblist += ['mvec', 'm']

# define absolute paths
root_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
include_folder = os.path.join(root_folder, "include")
classy_folder = os.path.join(root_folder, "python")

# Recover the CLASS version
with open(os.path.join(include_folder, 'common.h'), 'r') as v_file:
    for line in v_file:
        if line.find("_VERSION_") != -1:
            # get rid of the " and the v
            VERSION = line.split()[-1][2:-1]
            break

setup(
    name='classy',
    version=VERSION,
    description='Python interface to the Cosmological Boltzmann code CLASS',
    url='http://www.class-code.net',
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("classy", [os.path.join(classy_folder, "classy.pyx")],
                           include_dirs=[nm.get_include(), include_folder],
                           libraries=liblist,
                           library_dirs=[root_folder, ],
                           extra_link_args=' -fopenmp'.split(),  #['-lgomp'],
                           )],
    #data_files=[('bbn', ['../bbn/sBBN.dat'])]
)

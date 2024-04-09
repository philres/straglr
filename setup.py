import os
import sys
from setuptools import setup, find_packages
#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/stragler')

from straglr import __version__

setup(
    name='straglr',
    version=__version__,
    description='Straglr',
    long_description='Short tandem repeat genotyping using long reads',
    url='https://github.com/bcgsc/straglr.git',
    author='Readman Chiu',
    author_email='rchiu@bcgsc.ca',
    license='BCCA',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
    packages=['straglr'],
    install_requires = [
        'pysam==0.22.0',
        'pybedtools==0.9.1',
        'numpy==1.26.4',
        'pathos==0.3.2',
        'scikit-learn==1.4.0',
        'scipy==1.13.0',
        'natsort==8.4.0'
        ],
    entry_points ={
        'console_scripts': [
            'straglr-genotype=straglr.straglr_genotype:main'
        ]
    }
)

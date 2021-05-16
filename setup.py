"""
    Setup file for gwas2vcf library. Licensed under the MIT.
"""

import sys

from Cython.Distutils import build_ext
from setuptools import setup

if sys.version_info < (3, 7):
    sys.exit(
        "Sorry, Python 3.7 or newer is required to install and run gwas2vcf")

install_requires = [
    "pysam==0.15.2",
    "biopython==1.72",
    "marshmallow==2.18.1",
    "numpy==1.15.4",
    "vgraph @ git+git://github.com/SelfHacked/vgraph@v1.4.0#egg=vgraph",
]
setup_requires = ["setuptools_scm==1.15.0", "setuptools_scm_git_archive==1.0"]
tests_require = ["pytest==5.3.5"]

classifiers = """
Development Status :: 2 - Alpha
Programming Language :: Python
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Bioinformatics
"""

if __name__ == "__main__":
    setup(
        name="gwas2vcf",
        version="1.3.2",
        description="Convert GWAS summary statistics to VCF",
        url="https://github.com/SelfHacked/gwas2vcf",
        license="MIT",
        classifiers=classifiers.split("\n"),
        use_scm_version=True,
        zip_safe=False,
        tests_require=tests_require,
        py_modules=['main', 'param', 'gwas', 'vcf'],
        install_requires=install_requires,
        cmdclass={"build_ext": build_ext},
        entry_points={"console_scripts": ["gwas2vcf=main:main"]},
    )

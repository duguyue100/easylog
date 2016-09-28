"""Setup script for the easylog package.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from setuptools import setup

classifiers = """
Development Status :: 2 - Pre-Alpha
Environment :: Console
Intended Audience :: Science/Research
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: MacOS
Operating System :: POSIX :: Linux
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Topic :: Utilities
Topic :: Scientific/Engineering
Topic :: Software Development :: Libraries :: Python Modules
"""

try:
    from simretina import __about__
    about = __about__.__dict__
except ImportError:
    about = dict()
    exec(open("easylog/__about__.py").read(), about)

setup(
    name="easylog",
    version=about["__version__"],

    author=about["__author__"],
    author_email=about["__author_email__"],

    url=about["__url__"],
    download_url=about["__download_url__"],

    packages=["easylog"],
    # package_data={"easylog": ["retina-data/*.*"]},
    scripts=["script/elog"],

    classifiers=list(filter(None, classifiers.split('\n'))),
    description="A minimum logger for experiments."
)

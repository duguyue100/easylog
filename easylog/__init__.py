"""Init file for easylog.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
import os
import sys
from os.path import join, isdir

from easylog.utils import *

HOME_PATH = os.environ["HOME"]
EASYLOG_PATH = join(HOME_PATH, ".easylog")
RUNNING_PYTHON = sys.version_info[0]

# create resource folder if not existed.
if not isdir(EASYLOG_PATH):
    os.makedirs(EASYLOG_PATH)

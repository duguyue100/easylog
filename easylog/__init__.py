"""Init file for easylog.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

import os
from os.path import join, isdir

HOME_PATH = os.environ["HOME"]
EASYLOG_PATH = join(HOME_PATH, ".easylog")

# create resource folder if not existed.
if not isdir(EASYLOG_PATH):
    os.makedirs(EASYLOG_PATH)

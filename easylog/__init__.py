"""Init file for easylog.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
import os
import sys
from os.path import join, isdir

try:
    import telegram
    from telegram.bot import Bot
    TELEGRAM_STATUS = True
    print ("[MESSAGE] The telegram service is switched on.")
except ImportError:
    print ("[MESSAGE] The telegram service is switched off.")
    TELEGRAM_STATUS = False

from easylog.utils import *

HOME_PATH = os.environ["HOME"]
EASYLOG_PATH = join(HOME_PATH, ".easylog")
RUNNING_PYTHON = sys.version_info[0]

# create resource folder if not existed.
if not isdir(EASYLOG_PATH):
    os.makedirs(EASYLOG_PATH)

# setup the telegram parameters
TELEGRAM_TOKEN_PATH = join(EASYLOG_PATH, "tokens")

if not isdir(TELEGRAM_TOKEN_PATH):
    os.makedirs(TELEGRAM_TOKEN_PATH)
    print ("[MESSAGE] The telegram token path is create at %s" %
           (TELEGRAM_TOKEN_PATH))

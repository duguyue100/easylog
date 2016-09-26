"""Streaming from standard output.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
import time

while True:
    print ("[MESSAGE] Hello World ", time.time())
    time.sleep(1.5)

#!/usr/bin/env python
"""The central routine of easylog.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
import argparse

def easylog_main(file_name, extra_args):
    """The main function for running easylog tool.

    Parameters
    ----------
    file_name : string
        the script that you want to monitor.
    extra_args: string
        the extra arguments from the script you want to log.
    """
    print (file_name)
    print (extra_args)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A minimum logger for "
                                     "experiments by Yuhuang Hu")

    parser.add_argument("--file-name", "-f", type=str,
                        help="The script that you want to log.")
    parser.add_argument("--extra-args", "-e", type=str,
                        default="",
                        help="Extra arguments that are for the scripts.")

    args = parser.parse_args()

    easylog_main(**vars(args))

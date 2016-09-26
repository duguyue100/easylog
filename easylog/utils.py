"""Utility functions for easylog.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
import easylog


def split_args(args):
    """Split arguments string from input.

    Parameters
    ----------
    args : string
        arguments string that typically splitted by spaces.
    Parameters
    ----------
    args_dict : list
        the list of the splited arguments.
    """
    return args.split(" ")

#! /usr/bin/env python3

import sys

def banner():
    try:
        from colorama import Fore, Style

        i_dot = Fore.RED + '(_)'
        i_dot_top = Fore.RED + '_'
        color_reset = Style.RESET_ALL
        print("\
                           _         _ {}{}       \n \
            __      _____| |__   __| {}{}_ __  \n \
            \ \ /\ / / _ \ '_ \ / _` | | '__| \n \
             \ V  V /  __/ |_) | (_| | | |    \n \
              \_/\_/ \___|_.__/ \__,_|_|_|   v0.1.0 \n\n \
                                            Created by N3NU\n".format(i_dot_top, 
                                            color_reset, i_dot, color_reset))
    except:
        print("\
                           _         _ _       \n \
            __      _____| |__   __| (_)_ __  \n \
            \ \ /\ / / _ \ '_ \ / _` | | '__| \n \
             \ V  V /  __/ |_) | (_| | | |    \n \
              \_/\_/ \___|_.__/ \__,_|_|_|   v0.1.0 \n\n \
                                            Created by N3NU\n")
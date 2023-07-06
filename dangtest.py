# SPDX-FileCopyrightText: 2023 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from dang import wrapper


def main(stdscr):
    while True:
        print(repr(stdscr.getkey()))


wrapper(main)

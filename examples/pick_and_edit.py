# SPDX-FileCopyrightText: 2023 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from adafruit_editor import editor, picker

while True:
    try:
        filename = picker.pick_file()
    except KeyboardInterrupt:
        break

    try:
        editor.edit(filename)
    except KeyboardInterrupt:
        pass

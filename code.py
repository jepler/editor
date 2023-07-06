# SPDX-FileCopyrightText: 2023 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import editor
import picker

while True:
    filename = picker.pick_file()
    try:
        editor.edit(filename)
    except KeyboardInterrupt:
        pass

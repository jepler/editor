import picker, editor
try:
    filename = picker.pick_file()
    editor.edit(filename)
except KeyboardInterrupt:
    pass

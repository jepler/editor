import picker, editor
while True:
    filename = picker.pick_file()
    try:
        editor.edit(filename)
    except KeyboardInterrupt:
        pass

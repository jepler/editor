from dang import wrapper

def main(stdscr):
    while True:
        print(repr(stdscr.getkey()))

wrapper(main)

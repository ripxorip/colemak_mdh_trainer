import argparse
import curses
import os

class Trainer():
    def __init__(self, win):
        self.win = win
        self.win.nodelay(True)
        self.win.clear()

    def get_colemak_dmk_layout(self):

    def handle_input(self, key):
        self.set_output(str(key))

    def set_output(self, out_str):
        self.win.clear()
        self.win.addstr(out_str)

    def run(self):
        while 1:
            try:
               key = self.win.getkey()
               self.handle_input(key)
            except Exception as e:
               # No input
               pass

def main(win):

    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    parser = argparse.ArgumentParser(description='Tool to practice touch typing on my new ergo..')
    parser.add_argument('-b', '--buildcmd', help='Command used to build the project', required=False, nargs='+')
    args = parser.parse_args()

    t = Trainer(win)
    t.run()

curses.wrapper(main)

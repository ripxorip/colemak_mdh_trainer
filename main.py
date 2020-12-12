import argparse
import curses
import os

class Trainer():
    def __init__(self, win):
        self.win = win

    def train(self):
        self.win.nodelay(True)
        key=""
        self.win.clear()
        self.win.addstr("Detected key:")
        while 1:
            try:
               key = self.win.getkey()
               self.win.clear()
               self.win.addstr("Detected key:")
               self.win.addstr(str(key))
               if key == os.linesep:
                  break
            except Exception as e:
               # No input
               pass

def main(win):
    parser = argparse.ArgumentParser(description='Tool to practice touch typing on my new ergo..')
    parser.add_argument('-b', '--buildcmd', help='Command used to build the project', required=False, nargs='+')
    args = parser.parse_args()
    print(args)

    t = Trainer(win)
    t.train()

curses.wrapper(main)

import random
import argparse
import curses
import os

def split(word):
        return [char for char in word]

class Trainer():
    def __init__(self, win):
        self.win = win
        self.win.nodelay(True)
        self.win.clear()

    def set_colemak_dmk_layout(self):
        ret = []
        ret.append(split('1234567890'))
        ret.append(split('qwfpbjluy;'))
        ret.append(split('arstgmneio'))
        ret.append(split('zxcdvkh,./'))
        self.layout = ret

    def handle_input(self, key):
        if len(self.inp) == 0:
            if self.test_seq[0] == key:
                char_ok = True
            else:
                char_ok = False
        elif self.test_seq[len(self.inp)] == key:
            char_ok = True
        else:
            char_ok = False

        if char_ok:
            self.inp += key

        self.win.erase()

        self.win.addstr('[ ', curses.color_pair(103))
        for i in range(0, 4):
            self.win.addstr(self.letters_to_test[i], curses.color_pair(103))

        self.win.addstr('   ', curses.color_pair(103))

        for i in range(4, 8):
            self.win.addstr(self.letters_to_test[i], curses.color_pair(103))
        self.win.addstr(' ]\n', curses.color_pair(103))

        for i in range(0, len(self.inp)):
            self.win.addstr(self.test_seq[i], curses.color_pair(71))

        if not char_ok:
            self.win.addstr(self.test_seq[len(self.inp)], curses.color_pair(197))
            start = len(self.inp)+1
        else:
            start = len(self.inp)

        for i in range(start, len(self.test_seq)):
            self.win.addstr(self.test_seq[i], curses.color_pair(103))

        if self.test_seq[len(self.inp)] == ' ':
            self.inp += ' '

        if (len(self.inp) == len(self.test_seq)):
            self.generate_test_seq()
            self.set_output(t.test_seq)

    def set_output(self, out_str):
        self.win.clear()
        self.win.addstr('[ ', curses.color_pair(103))
        for i in range(0, 4):
            self.win.addstr(self.letters_to_test[i], curses.color_pair(103))

        self.win.addstr('   ', curses.color_pair(103))

        for i in range(4, 8):
            self.win.addstr(self.letters_to_test[i], curses.color_pair(103))
        self.win.addstr(' ]\n', curses.color_pair(103))

        self.win.addstr(out_str)

    def run(self):
        while 1:
            try:
               key = self.win.getkey()
               self.handle_input(key)
            except Exception as e:
               # No input
               pass

    def generate_test_seq(self):
        num_words = 8

        letters_to_test = self.layout[2][0:4]
        letters_to_test.extend(self.layout[2][6:])

        self.letters_to_test = letters_to_test

        test_str = ''
        for i in range(0, num_words):
            wordlen = random.randint(2, 4)
            for j in range(0, wordlen):
                test_str += (letters_to_test[random.randint(0, len(letters_to_test)-1)])
            test_str += ' '

        self.test_seq = test_str
        self.inp = ''


def main(win):

    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    parser = argparse.ArgumentParser(description='Tool to practice touch typing on my new ergo..')
    parser.add_argument('-b', '--buildcmd', help='Command used to build the project', required=False, nargs='+')
    args = parser.parse_args()

    t = Trainer(win)
    t.set_colemak_dmk_layout()
    t.generate_test_seq()
    t.set_output(t.test_seq)
    """
    for i in range(0, 255):
        win.addstr(str(i) + ' ', curses.color_pair(i))
    """
    t.run()

curses.wrapper(main)

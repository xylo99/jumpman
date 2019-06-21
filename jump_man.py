#!/usr/bin/env python3
import sys
import time
import numpy
import shutil
import pandas
import scipy.constants

class Player:
    def __init__(self, ceil_h, x_pos, yh_pos):
        self.ch = ceil_h #Represents the height of the ceiling from the ground.
        self.x = x_pos #The random xpos that's assigned at initialization
        self.yh = yh_pos #The distance from the head to the ceiling
        self.jm = [' o ','/','|', '\\', '/','\\']
        self.head = self.jm[0]
        self.middle = ''.join(map(str, self.jm[1:4]))
        self.tail = ' '.join(map(str, self.jm[4:6]))
        self.ypos = 0

    def set_ypos(self, ypos):
        self.ypos = ypos

    def get_ypos(self):
        return self.ypos

    def print_head(self):
        print(self.head, end='')

    def print_middle(self):
        print(self.middle, end='')

    def print_tail(self):
        print(self.tail, end='')

    def get_head(self):
        return self.jm[0]

    def get_middle(self):
        return self.middle

    def get_tail(self):
        return self.tail

    def print_next_section(self, which, inline):
        if inline:
            sys.stdout.write(u'\u001b[' + str(1) + 'B')
            sys.stdout.write(u'\u001b[' + str(3) + 'D')
            print(which, end='')
        else:
            print('\n' + which)

    def print_at_pos(self, section, x_pos=0, y_pos=0, reset_x=False, reset_y=False):
        if x_pos == 0 and y_pos == 0:
            print(section[0])
            self.print_next_section(section[1], False)
            self.print_next_section(section[2], False)
        elif x_pos == 0 and y_pos > 0:
            sys.stdout.write(u'\u001b[' + str(y_pos) + 'A')
            print(section[0])
            self.print_next_section(section[1], False)
            self.print_next_section(section[2], False)
            if reset_y:
                sys.stdout.write(u'\u001b[' + str(y_pos) + 'B')
        elif x_pos == 0 and y_pos < 0:
            sys.stdout.write(u'\u001b[' + str(-y_pos) + 'B')
            sys.stdout.write((section[0]))
            self.print_next_section(section[1], False)
            self.print_next_section(section[2], False)
            print()
            if reset_y:
                sys.stdout.write(u'\u001b[' + str(-y_pos + 3) + 'A')
        elif x_pos > 0 and y_pos == 0:
            sys.stdout.write(u'\u001b[' + str(x_pos) + 'C')
            print(section[0], end='')
            self.print_next_section(section[1], True)
            self.print_next_section(section[2], True)
            print()
        elif x_pos < 0 and y_pos == 0:
            sys.stdout.write(u'\u001b[' + str(-x_pos) + 'D')
            print(section[0], end='')
            self.print_next_section(section[1], True)
            self.print_next_section(section[2], True)
            if reset_x:
                sys.stdout.write(u'\u001b[' + str(-x_pos) + 'D')
            if reset_y:
                sys.stdout.write(u'\u001b[' + str(y_pos + 3) + 'B')
        elif x_pos < 0 and y_pos > 0:
            sys.stdout.write(u'\u001b[' + str(-x_pos) + 'D')
            sys.stdout.write(u'\u001b[' + str(y_pos) + 'A')
            print(section[0], end='')
            self.print_next_section(section[1], True)
            self.print_next_section(section[2], True)
            if reset_x:
                sys.stdout.write(u'\u001b[' + str(-x_pos) + 'C')
            if reset_y:
                sys.stdout.write(u'\u001b[' + str(y_pos + 3) + 'B')
        elif x_pos > 0 and y_pos > 0:
            sys.stdout.write(u'\u001b[' + str(x_pos) + 'C')
            sys.stdout.write(u'\u001b[' + str(y_pos) + 'A')
            print(section[0], end='')
            self.print_next_section(section[1], True)
            self.print_next_section(section[2], True)
            if reset_x:
                sys.stdout.write(u'\u001b[' + str(x_pos) + 'D')
            if reset_y:
                sys.stdout.write(u'\u001b[' + str(-y_pos + 3) + 'B')
        elif x_pos > 0 and y_pos < 0:
            sys.stdout.write(u'\u001b[' + str(x_pos) + 'C')
            sys.stdout.write(u'\u001b[' + str(-y_pos) + 'B')
            sys.stdout.write(section[0])
            self.print_next_section(section[1], True)
            self.print_next_section(section[2], True)
            if reset_x:
                sys.stdout.write(u'\u001b[' + str(x_pos) + 'D')
            if reset_y:
                sys.stdout.write(u'\u001b[' + str(-y_pos + 3) + 'A')
        elif x_pos < 0 and y_pos < 0:
            sys.stdout.write(u'\u001b[' + str(-x_pos) + 'D')
            sys.stdout.write(u'\u001b[' + str(-y_pos) + 'B')
            print(section[0], end='')
            self.print_next_section(section[1], True)
            self.print_next_section(section[2], True)
            if reset_x:
                sys.stdout.write(u'\u001b[' + str(-x_pos) + 'D')
            if reset_y:
                sys.stdout.write(u'\u001b[' + str(-y_pos + 3) + 'A')

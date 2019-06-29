#!/usr/bin/env python3
import jump_man
import subprocess
import random
import shutil
import time
import sys

#Erase the printed text by moving the courser up one
#@param s_state is starting state
def erase_jm(amount, s_state=False):
    i = 0
    sys.stdout.write(u'\u001b[' + str(amount+3) + 'B')
    if not s_state:
        while i <= amount:
            sys.stdout.write('\x1b[2K')
            sys.stdout.write(u'\u001b[' + str(0) + 'A') #Move courser up by one
            sys.stdout.write('\x1b[2K')
            i += 1
        sys.stdout.write(u'\u001b[' + str(amount+3) + 'B')
    else:
        while i <= amount + 3:
            sys.stdout.write('\x1b[2K')
            sys.stdout.write(u'\u001b[' + str(0) + 'A')
            sys.stdout.write('\x1b[2K')
            i += 1


#wrapper function to the jumpman class
def jump(count, ceil_h, x_pos, hdist):
    s_area = shutil.get_terminal_size().columns
    pos = s_area - (s_area - x_pos)
    men = []
    for i in range(count):
        men.append(jump_man.Player(ceil_h, x_pos, hdist)) #args are:  ceiling height, x_pos, dist from head to ceil.

    player = []
    for i in range(count):
        men[i].set_ypos(i)
        player.append(men[i].get_head())
        player.append(men[i].get_middle())
        player.append(men[i].get_tail())
        men[i].print_at_pos(player, 2, -ceil_h, False, True)

    sys.stdout.flush()
    time.sleep(1)
    erase_jm(ceil_h, False)
    time.sleep(1)
    sys.stdout.write(u'\u001b[' + str(s_area) + 'D')
    sys.stdout.write(u'\u001b[' + str(3) + 'A')
    sys.stdout.flush()

    for i in range(count):
        num = list(range(1, ceil_h))
        random.shuffle(num)
        y = num.pop()
        men[i].set_ypos(y)
        men[i].print_at_pos(player, 2, y+2, False, True)

    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(u'\u001b[' + str(s_area + 3) + 'D')

if __name__=='__main__':
    subprocess.run(['clear'])
    for i in range(5):
        jump(7, 20, 10, 10)
        subprocess.run(['clear'])

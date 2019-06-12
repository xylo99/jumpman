#!/usr/bin/env python3
import numpy
import pandas
import scipy.constants
import shutil

class Player:
    def __init__(self, ceil_h, x_pos, yh_pos):
        self.ch = ceil_h #Represents the height of the ceiling from the ground.
        self.x = x_pos #The random xpos that's assigned at initialization
        self.yh = yh_pos #The distance from the head 
    
    #The corresponding test for this function is test1  
    #Print the jumpman on the x-axis at specified x position  
    def print_jm(self):
        jm = ['o','/','|', '\\', '/','\\']
        head = jm[0]
        middle = ''.join(map(str, jm[1:4]))
        tail = ' '.join(map(str, jm[4:6]))
        if self.x > 0:
            s_area = shutil.get_terminal_size().columns
            player = ' ' + head + '\n' + middle + '\n ' + tail
            print(head.center((s_area//2) - ((s_area//2) - self.x)))
            print(middle.center((s_area//2) - ((s_area//2) - self.x)))
            print(tail.center((s_area//2) - ((s_area//2) - self.x)))
    
    #Note: this erases all of the jumpmen because of line 37 (5th line in function)
    #TODO: add three conditions (named cond in param):
    #      The first condition is when the initial jump happens. All jumpmen are erased for their reprinting
    #      The second condition is after the jumpmen are reprinted after an attempted jump. Every jumpmen gets erased. Thus we erase each line that's under the ceiling.
    def erase_jm(cond, bot):
        if cond == 'start':
            for n in range(3):
                sys.stdout.write(u'\u001b[' + str(n) + 'A')
                sys.stdout.write(u'\033[K')
                print('')
        elif cond == 'end':         
            ypos = self.yh
            for n in range(ypos-3):
                sys.stdout.write(u'\u001b[' + str(n) + 'A') #move courser down by one
                sys.stdout.write(u'\033[K') #erase entire line.
                print('')
        
        

    #The program must get better at using this function
    #@param (float) what the program will guess. 
    def jump(self, guess):
        result = check_guess(guess) #This function will return how close you are to the answer. It's possible to be too low/high.
        dist_frm_ceil = self.ch
        erase_jm

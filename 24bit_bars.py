#!/usr/bin/env python3
# print out 24 bit vertical color bars, compatible with putty 0.71
# or any modern Linux/Unix terminal or shell
# width of ts.columsn / 7, length of 255 / terminal rows/lines
###
import os

def print_color(red=0,green=0,blue=0,counter=1):
    out=''
    for a in range(0,counter):
        out = str.format("\033[48;2;{};{};{}m ",red,green,blue)
        print(out,end='')
    return

def reset_color():
    print(str.format("\033[0m"))

def rgb_loop():
    ts = os.get_terminal_size()
    bar_width = int(ts.columns / 7 )
    bar_length = int(255 / ts.lines )
#    bar_length = 1 # uncomment if you want to see all 255 lines
    for x in range(255,0,bar_length * -1):
        print_color(red=x,green=x,blue=x,counter=bar_width) #greyscale
        print_color(red=x,counter=bar_width) #red
        print_color(green=x,counter=bar_width) #green
        print_color(blue=x,counter=bar_width) #blue
        print_color(red=x,blue=x,counter=bar_width) #magenta
        print_color(red=x,green=x,counter=bar_width) #yellow
        print_color(green=x,blue=x,counter=bar_width) #cyan
        reset_color()

rgb_loop()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------#
__author__ = "Werner Suchowitzki Orozco"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Werner Suchowitzki Orozco"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Werner Suchowitzki Orozco"
__email__ = "wsuchowitzki@stengineeringsolutions.com"
__status__ = "Init"

#------------------------------------------------------------------------------#
#LIBRARIES:
import random
import binascii
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#FUNCTIONS:
def menu():
    option = input("""
    Code3 Bitwise:
    1) AND
    2) OR
    3) XOR
    4) Shift
    Option: """)

    return(option)


def bitwise(case):
    list = [0x0f,0x10,0xa0,0xaa,0x01,0xba,0x00,0x52,0xcc,0xca,\
            0x0f,0x10,0xa0,0xaa,0x01,0xba,0x00,0x52,0xcc,0xca]

    list2 = []

    mask = 0x01

    print("List:")
    print('[{}]'.format(', '.join(hex(x) for x in list)))

    if case == '1':
        print(case)

        #AND
        for pos in list:
            list2.append(pos & mask)

        print("AND:")

    elif case == '2':
        #OR
        for pos in list:
            list2.append(pos | mask)
        
        print("OR:")

    elif case == '3':
        #XOR
        for pos in list:
            list2.append(pos ^ mask)
        
        print("XOR:")

    elif case == '4':
        #Shift
        shift = int(input("Shift number: "))
        for pos in list:
            list2.append(pos << shift)
        
        print("Shift:")

    else:
        print("Incorrect option")

    print('[{}]'.format(', '.join(hex(x) for x in list2)))

#------------------------------------------------------------------------------#
#MAIN
if __name__ == "__main__":
    switch = menu()
    bitwise(switch)
#------------------------------------------------------------------------------#

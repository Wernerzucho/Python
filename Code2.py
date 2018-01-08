#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------
__author__ = "Werner Suchowitzki Orozco"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Werner Suchowitzki Orozco"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Werner Suchowitzki Orozco"
__email__ = "wsuchowitzki@stengineeringsolutions.com"
__status__ = "Init"

#--------------------------------------------------------
#LIBRARIES:
import random
#-------------------------------------------
# -------------
#FUNCTIONS:
class MyFirstClass():

    def __init__(self):
        self.list1 = [1,2,3,4,5,6,7,8,9,10]
        self.list2 = []
        self.a = 5
        self.b = random.randint(1,10)

    def funct1(self):
        if(self.a == self.b):
            print(self.b)
            print("I´m winner")
        else:
            print(self.b)
            print("I´m loser")


    def funct2(self):
        for i in self.list1:
            self.list2.append(i)
            print(i)
        
        print(len(self.list1))
        print(len(self.list2))

        random.shuffle(self.list2)
        if(self.list2[5] == 6):
            print("Correct")
        else:
            print("Fail")



#-------------------------------------------------------
#MAIN
if __name__ == "__main__":
    obj = MyFirstClass()
    obj.funct1()
    obj.funct2()
#-----------------------------------------------------
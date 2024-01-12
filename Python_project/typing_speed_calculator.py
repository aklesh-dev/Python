# calculate the typing speed.
from time import *
import random as r

def mistake(pargtext, usertest):
    error = 0
    for i in range(len(pargtext)):
        try:
            if pargtext[i] != usertest[i]:
                error -= -1
        except :
            error -= -1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

test = ["A paragraph is a group of sentences that fleshes out a single idea.",
        "My name is Aklesh Yadav", 
        "Python is a high-level programming language designed to be easy to read and simple to implement.",
        "It is open source, which means it is free to use, evenfor commercial applications."
        ]
test1 = r.choice(test)
title = "*****          Typing Speed Calculator         *****"
print(title)
print('_'*len(title))
print()
print(test1)
print()
time1 = time()
testinput = input(" Enter : ")
time2 = time()

print("Speed : ", speed_time(time1, time2, testinput), "word/sec")
print("Error : ", mistake(test1, testinput))

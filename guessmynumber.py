# The first program for HITES: Hello Android

import android
d = android.Android()

##### Don't change anything above this line #####

x = 0
z = 0
from random import randint
x = randint(1,50)
y = 0
print("Guess my number. It is between 1 and 50.")
while z != x:
    z = int(raw_input("Input your guess: "))
    y = y+1
    if z == x:
        d.ttsSpeak("You got it!")
        print "It took you {0} tries.".format(y)
        break
    elif z<x:
        print("Too low.")
        d.ttsSpeak("too low")
        d.vibrate(1000)
    elif z>x:
        print("Too high.")
        d.ttsSpeak("too high")
        d.vibrate(1000)
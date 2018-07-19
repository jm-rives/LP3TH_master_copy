#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-


print("""*
You enter a dark room with two doors.
Do you take door number 1 or door number 2?
*
""")

door = input("Please enter 1 or 2: ")

if door == '1':
    print("""
    *
    There's a giant bear here eating a cheese cake.
    What do you do now?
    1. Take the cake.
    2. Scream at the bear.
    *""")

    bear = input("Please enter 1 or 2: ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better. \n The bear runs away.")

elif door == '2':
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("""
    *
    1. Blueberries. Blueberries are so nice.
    2. Yellow jacket clothespins.
    3. Understanding revolvers yelling melodies.
    *""")

    insanity = input("Please enter 1,  2, or 3: ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
    else:
        print("The insanity rots your eyes into a pool of muck.")
else:
    print("You stumble around and fall on a knife and die. Good job!")

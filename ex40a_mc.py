#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7tangerine
# -*- coding: utf-8 -*-

# import a method from another file
# import mystuff
# mystuff.apple()
# # # second wave of exercise
# print(mystuff.tangerine)

## accessing a tuple
# mystuff = {'apple': "I AM APPLES!"}
# print("This is from the tuple: ",  mystuff['apple'])

# third wave of exercise

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

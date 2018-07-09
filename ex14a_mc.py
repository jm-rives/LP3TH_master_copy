#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
from sys import argv
from string import Template

program, name = argv
prompt ='🐢 '

script = str(program)
user_name = str(name)

a = Template("Hi $user_name, I'm the $script script.")
print(a.substitute(user_name=user_name, script=script))

print("I'd like to ask you a few questions.")

b = Template("Do you like me $user_name?")
print(b.substitute(user_name=user_name))
likes = input(prompt)

c = Template("Where do you live $user_name?")
print(c.substitute(user_name=user_name))
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

t = Template("""
Alright, so you said '$likes' about liking me.
You live in $lives. Not sure where that is.
And you have a $computer computer. Nice.
""")
print(t.substitute(likes=likes, lives=lives, computer=computer))

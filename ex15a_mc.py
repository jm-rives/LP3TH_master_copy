#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
from string import Template
from sys import argv

script, filename = argv

program = script
file = filename

txt = open(file)

t = Template("Here's your file $file: ")
print(t.substitute(file=file))
print(txt.read())

file_again = input("🚀  ")

txt_again = open(file_again)
print(txt_again.read())

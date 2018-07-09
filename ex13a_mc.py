# Would this script be effective in sanitizing argvs?

from string import Template
from sys import argv

script, first, second, third = argv

file = str(script)
two = str(first)
three = str(second)
four = str(third)



index0 = Template("Your script is $file.")
index1 = Template("Your first variable is $two.")
index2 = Template("Your second variable is $three.")
index3 = Template("Your third variable is $four.")

print(index0.substitute(file=file))
print(index1.substitute(two=two))
print(index2.substitute(three=three))
print(index3.substitute(four=four))

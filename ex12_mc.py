from string import Template

age = input("How old are you? ")
height = input("How tall are you in inches? ")
weight = input("How much do you weigh? ")

t = Template("So you are $age, $height inches tall, and weigh $weight pounds.")
print(t.substitute(age=age, height=height, weight=weight))
    

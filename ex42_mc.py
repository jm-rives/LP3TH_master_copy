#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
## Animal is-a object (yes, sort of confuing look at the extra credit)
class Animal(object):
    pass

## Dog is a class that inherits certain traits from it's parent class Animal
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Ditto
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name
## ??
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind (sorta if cat 😉 )
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):

        ## What is this witch craft?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 1200000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()

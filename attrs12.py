import attr
from cs50 import *
#attrs is the Python package that will bring back the joy of writing classes by relieving you from the drudgery of implementing object protocols (aka dunder methods). Trusted by NASA for Mars missions since 2020!
#Its main goal is to help you to write concise and correct software without slowing down your code.
#For that, it gives you a class decorator and a way to declaratively define the attributes on that class:


@attr.s
class Person(object):
    ages = get_int("please enter your age: ")
    if ages >= 18:
        name = attr.ib(default='albert')
        surname = attr.ib(default='twayigize')
        age = attr.ib(default=ages)
    else:
        print("your not allowed ")
p = Person()
print(p)
p = Person('messi', 'ronarido')
p.age = 60
print(p)

p = Person()
print(p)
p.age = 28
print(p)
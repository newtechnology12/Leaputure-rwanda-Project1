#ninja2 is a python template engine need to create html, xml or other markup format that are returtner to the user via an http response
#code example
from jinja2 import *
from cs50 import *
name = get_string("Enter your name: ")
email = get_string("please enter your email: ")
age = get_int("enter your age: ")

names = Template("Hello {{ name }}")
emal = Template("your email {{ email }}")
ages = Template("you have age {{ age }}")
msg = names.render(name=name)
emal = names.render(email=email)
ages = names.render(age=age)

print(msg+': your email is: '+email+': //and you have ', str(ages))
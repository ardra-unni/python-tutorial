#user define modules

import mymodule
print(mymodule.greet("ardra"))
print(mymodule.greet1("zahra"))
print(mymodule.greet2("momo"))

from mymodule import greet1
print (greet1("zahra"))

import mymodule as m
print(m.greet("ardra"))
print(m.greet1("zahra"))
print(m.greet2("momo"))

# built-in modules

import math
print(math.factorial(5))
print(math.sqrt(25))
print(math.pi)

import datetime
now=datetime.datetime.now()
print(now)

import os
current_dir=(os.getcwd)
print(current_dir)

import sys
print(sys.version)

import random
a=random.randint(1,10)
print(a)

#thirdparty library
import numpy as np
a=np.array([1,2,3,4])
print(a)
print(type(a))



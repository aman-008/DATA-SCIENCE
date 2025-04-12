# Two types of module in Python:
# 1. Built-in modules
# 2. External modules
# List of all the built-in module-- https://docs.python.org/3/py-modindex.html

import math
import os
import mymodule
import requests
print(math.sqrt(25))

mymodule.hello()

r = requests.get("https://www.google.com")
print(r.text)
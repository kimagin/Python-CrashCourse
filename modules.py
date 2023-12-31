# NOTE: A module is basically a file containing a set of functions to include
# in your application. There are core Python modules, modules you can install
# using the pip package manager (including Django) as well as custom modules.


# PERF: Import the module

# import datetime
# import time

# PERF: Import pip3 modules
# from camelcase import CamelCase

# PERF: Import the module partially
from datetime import date
from time import time


# today = datetime.date.today()
today = date.today()


# timestamp = time.time()
timestamp = time()

# c = CamelCase()

# print(c.hump('hello world of camel case'))

print(today, timestamp)

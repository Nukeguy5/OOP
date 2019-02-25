
from enum import Enum
from collections import namedtuple

# ENUM
UserEnum = Enum('UserIn', input('Enter Input Seperated by Spaces: '))

# TUPLE
Tup = namedtuple('namedTup', "name value")

# INPUT
UserFind = input('Enter Name to Find: ')

# FOR
for i in UserEnum:
    # FIND
    if i.name == UserFind:
        # ASSIGN
        tup = Tup(i.name, i.value)

# PRINT
print(f'name: {tup.name} value: {tup.value}')

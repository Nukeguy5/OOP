
from enum import Enum
from collections import namedtuple

names = 'BEES BIRDS BALLOONS'

# UserIn = Enum('UserIn', input('Enter Input: '))
UserEnum = Enum('UserIn', names)

Tup = namedtuple('Tup', [i.name for i in UserEnum])

UserFind = input('Enter Name to Find: ')

for i in UserEnum:
    if i.name = UserFind:
        



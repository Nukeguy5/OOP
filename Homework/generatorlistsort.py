
## For personal record of first success
# def is_sorted(*lst):
#     if type(lst[0]) == list:
#         gen = (i for i in lst[0])
#     else:
#         gen = (i for i in lst)
#     first = next(gen)
#     return next_is_greater(gen, first)

# def next_is_greater(gen, curr):
#     nxt = next(gen)
#     try:
#         if curr <= nxt:
#             return next_is_greater(gen, nxt)
#         else:
#             return False
#     except StopIteration:
#         return True
#     except TypeError:
#         return False

from itertools import tee

class List:
    def __init__(self, *args):
        self.gen = (i for i in args)  # creates generator object
        self.gen1 = (i for i in args)
       
    def is_sorted(self):
        curr = next(self.gen)
        for i in self.gen:
            if curr >= i:
                return False
            curr = i
        return True

    def sort(self):
        self.gen1 = (i for i in sorted(list(self.gen1)))

    def ensure_sorted(self):
        if self.is_sorted():
            return "List is sorted."
        self.sort()
        print(self)
        return f'List is now sorted.'

    def __str__(self):
        return str(list(self.gen1))
  

my_list = List(1, 2, 3, 4, 5)
my_list2 = List(10, 2, 3, 4, 5)
print(my_list.ensure_sorted())
print(my_list2.ensure_sorted())

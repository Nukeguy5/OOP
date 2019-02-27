
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
       
    def is_sorted(self):
        gen = self.gen
        curr = next(gen)
        for i in gen:
            if curr >= i:
                return False
            curr = i
        return True

    def bubble_sort(self):
        [None for i in self.gen]
        lst = list(self.gen)
        for i in range(len(lst)-1, 0, 1):
            for j in range(len(lst)):
                if lst[i] > lst[j]:
                    temp = lst[j]
                    lst[j] = lst[i]
                    lst[i] = temp
        self.gen = (n for n in lst)
        return self.gen

    def ensure_sorted(self):
        if self.is_sorted():
            return "List is sorted."
        self.bubble_sort()
        print(self)
        return f'List is now sorted.'

    def append(self, *items):
        lst = list(self.gen)
        lst += items
        self.gen = (i for i in lst)

    def __str__(self):
        return str(list(self.gen))
  

my_list = List(1, 2, 3, 4, 5)
my_list2 = List(10, 2, 3, 4, 5)
print(my_list.ensure_sorted())
print(my_list2.ensure_sorted())

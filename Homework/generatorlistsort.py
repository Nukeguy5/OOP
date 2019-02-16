
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

class List:
    def __init__(self, *args):
        self.gen = (i for i in args)  # creates generator object
       
    def is_sorted(self):
        curr = next(self.gen)
        for i in self.gen:
            if curr >= i:
                return False
            curr = i
        return True

my_list = List(1, 2, 3, 4, 5)
my_list2 = List(1, 2, 10, 4, 5)
print(my_list.is_sorted())
print(my_list2.is_sorted())

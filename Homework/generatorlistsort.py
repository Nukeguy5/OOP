
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
        
def is_sorted(*lst):
    if type(lst[0]) == list:
        gen = (i for i in lst[0])
    else:
        gen = (i for i in lst)
    curr = next(gen)
    for i in gen:
        if curr >= i:
            return False
        curr = i
    return True

my_list = [i for i in range(10)]
my_list2 = [1, 2, 10, 3, 4]
print(is_sorted(my_list))
print(is_sorted(my_list2))

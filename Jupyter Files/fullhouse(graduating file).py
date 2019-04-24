
def isFullhouse(*args):
    num_dict = {}
    for i in args:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    
    if 2 in num_dict.values() and 3 in num_dict.values():
        return True
    return False

if __name__ == "__main__":
    print(isFullhouse(1, 1, 2, 2, 2))
    print(isFullhouse(1, 2, 2, 2, 2))
    print(isFullhouse(1, 2, 3, 4, 5))
    print(isFullhouse(3, 3, 1, 1, 1))
    print(isFullhouse(2, 2, 3, 4, 5))

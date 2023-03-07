import random
SIZE = 11

arr = [random.randint(-5,5) for i in range(SIZE)]


def recursiveSort(arr):
    if len(arr) == 1: # base case
        return arr
    half = len(arr)//2
    l = arr[:half]
    r = arr[half:]
    print("left:",l)
    print("right:",r)


    return recursiveSort(l) + recursiveSort(r)



print(arr)
recursiveSort(arr)



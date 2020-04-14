import random
import time
import sys


def merge(l, r):
    nl = len(l)
    nr = len(r)
    merged_arr = [0] * (nl + nr)

    i = 0
    j = 0

    while i < nl or j < nr:

        # if right side has remainder, add to list
        if i == nl:
            merged_arr[i+j] = r[j]
            j += 1
        # if left side has remainder, add to list
        elif j == nr:
            merged_arr[i+j] = l[i]
            i += 1
        # if left side[i] is smaller than right side[j], add to list and increment i
        elif l[i] <= r[j]:
            merged_arr[i+j] = l[i]
            i += 1
        # if right side[j] is smaller than left side[i], add to list and increment j
        else:
            merged_arr[i+j] = r[j]
            j += 1

    return merged_arr


def merge_sort(arr):
    n = len(arr)
    # return if only 1 elem in arr
    if n < 2:
        return arr
    #split in half
    mid = n//2
    l = arr[:mid]
    r = arr[mid:]

    return merge(merge_sort(l), merge_sort(r))


while True:
    n = input("\n\033[91mRandom list length: \033[00m")
    n = int(n)
    random_list = random.sample(range(n), n)
    b = time.time()
    merge_sort(random_list)
    e = time.time()

    print(f'\033[96mRuntime:\033[00m {e - b} seconds')


# STRETCH: implement an in-place merge sort algorithm
# IN-PLACE means more memory efficient, not creating a new array in memory
# make use of swaps for this


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

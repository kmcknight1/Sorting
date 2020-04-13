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
        # if left side[i] is larger than right side[j], add to list and increment i
        elif l[i] <= r[j]:
            merged_arr[i+j] = l[i]
            i += 1
        # if right side[j] is larger than left side[i], add to list and increment j
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


# STRETCH: implement an in-place merge sort algorithm
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

# STRETCH: implement Linear Search
def linear_search(arr, target):

  # TO-DO: add missing code

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls


'''
FROM CLASS - BINARY SEARCH CODE:
Binary Search is O(log(n))
Assume the array is sorted, return True if target is in the list
'''


def class_binary_search(arr, target):
    # set boundaries for low and high marks to search
    lo = 0
    hi = len(arr)
    # while low and high do not overlap...
    while lo < hi:
        # check the middle
        mid = (lo + hi) // 2
        # if equal, return True
        if arr[mid] == target:
            return True
        # else, if target is smaller
        elif target < arr[mid]:
            # set the high to the midpoint value
            hi = mid - 1
    # else, if target is bigger
        else:
            # set the low to midpoint value
            lo = mid + 1
    # if we get to the end, return False
    return False


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(class_binary_search(my_list, 30))
print(class_binary_search(my_list, 10))
print(class_binary_search(my_list, 8))

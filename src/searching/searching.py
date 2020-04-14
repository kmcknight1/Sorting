my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# STRETCH: implement Linear Search
def linear_search(arr, target):

    for i in arr:
        if i == target:
            return True

    return False


linear_search(my_list, 8)


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    lo = 0
    hi = len(arr)-1

    while lo < hi:
        mid = (lo + hi)//2

        if target == arr[mid]:
            return True
        elif target > arr[mid]:
            lo = arr[mid]
        else:
            hi = arr[mid]

    return False  # not found


binary_search(my_list, 8)


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return False  # array empty


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


print(class_binary_search(my_list, 30))
print(class_binary_search(my_list, 10))
print(class_binary_search(my_list, 8))


'''
Challenge from Training Kit:
Write a recursive search function that receives as input an array of 
integers and a target integer value. This function should return True 
if the target element exists in the array, and False otherwise.
'''


def recursive_search(arr, target):
    i = len(arr) - 1

    if i < 0:
        return False
    elif arr[i] == target:
        return True
    else:
        arr.pop()
        recursive_search(arr, target)


recursive_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6)

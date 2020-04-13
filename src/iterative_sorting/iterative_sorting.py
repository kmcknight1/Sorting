
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


my_list = [8, 4, 7, 1, 23, 9, 5, 6, 8, 1]

print(selection_sort(my_list))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr


my_list = [8, 4, 7, 1, 23, 9, 5, 6, 8, 1]


print(bubble_sort(my_list))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


'''
FROM CLASS - INSERTION SORT
'''


def insertion_sort(arr):
    # Divide your hand into sorted on the left and unsorted on the right
    # Sorted is just the first element
    # then go card by card and move them into place.
    # Loop through all elements in unsorted...
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i  # j is our sliding index
        # Shift sorted to the right until correct position found
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]  # Slide over one element
            j -= 1
        # Insert at that position
        arr[j] = temp
    return arr

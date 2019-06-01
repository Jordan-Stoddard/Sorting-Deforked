# TO-DO: Complete the selection_sort() function below 
"""
selection_sort takes in an array.
select the first index of the array and slice it into a new array.
select the new first index of the first array and compare it against each item in the new array from right to left
if it is smaller than the right most index, move to the left, if it is larger, insert there.
"""

def selection_sort( arr ):
    # loop through n-1 elements
    sorted = []
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
    return arr


"""

"""


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            left_side = arr[i]
            right_side = arr[i+1]
            if left_side > right_side:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if swapped == False:
            break
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr
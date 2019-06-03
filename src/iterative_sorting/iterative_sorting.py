# TO-DO: Complete the selection_sort() function below 
"""
Loop over array
set the first item in the array to be the current minimum
loop over each successive item in the array, and if the next item is lower than the current minimum
set that lower number to be the new current minimum
Once you've compared all the items, swap the current lowest minimum with the first item in the array.
Loop through again, this time starting with the first unsorted item in the list, and setting that to be the new current minimum.

"""

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_minimum = arr[i]
        for j in range(i + 1, len(arr)):
            cur_compare_item = arr[j]
            if cur_compare_item < cur_minimum:
                new_minimum_index = j
                cur_minimum = cur_compare_item
        if arr[i] > arr[new_minimum_index]:
            arr[i], arr[new_minimum_index] = arr[new_minimum_index], arr[i]
    
    


    return arr

print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


"""
bubble_sort takes in an array.
1) We initialize a boolean flag called swapped to be True
2) While swapped is True keep looping:
    *) First set swapped to false inside the while loop
    *) Then run a for loop, starting at 0 and going through the end of the array.
        >) Inside the for loop check to see if the left index is larger than the right index
            if it is swap, then set swapped to True
        >) Continue through for loop until end.
    *) Check if swapped == False, because if we didn't go into the if statement inside of the for loop
then that means no items swapped, which means the entire array is sorted from lowest to highest,
which means that swapped will == False, and the while loop will break
3) return the sorted version of the array.
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
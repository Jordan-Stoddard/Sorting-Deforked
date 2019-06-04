# TO-DO: complete the helper function below to merge 2 sorted leftys
def merge( leftA, rightA ):
    result = []
    while len(leftA) != 0 and len(rightA) != 0:
        if leftA[0] < rightA[0]:
            result.append(leftA[0])
            leftA.remove(leftA[0])
        else:
            result.append(rightA[0])
            rightA.remove(rightA[0])
    if len(leftA) == 0:
        result += rightA
    else:
        result += leftA
    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr)//2
        left_half =  merge_sort(arr[:middle])
        right_half = merge_sort(arr[middle:])
        return merge(left_half, right_half)

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr

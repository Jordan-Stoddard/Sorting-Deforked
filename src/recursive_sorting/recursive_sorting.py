# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    result = []
    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] < arrB[0]:
            result.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            result.append(arrB[0])
            arrB.remove(arrB[0])
    if len(arrA) == 0:
        result += arrB
    else:
        result += arrA
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

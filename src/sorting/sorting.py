# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    left = 0
    right = 0

    result = []

    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            result.append(arrA[left])
            left += 1
        else:
            result.append(arrB[right])
            right += 1

    while left < len(arrA):
        result.append(arrA[left])
        left += 1

    while right < len(arrB):
        result.append(arrB[right])
        right += 1

    return result


# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    mid = len(arr) // 2
    if len(arr) > 1:
        left = merge_sort(arr[0: mid])
        right = merge_sort(arr[mid:])
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

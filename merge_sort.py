def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)/2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    return combine(left, right)

def combine(arr1, arr2):
    result = []

    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    return result + arr1 + arr2

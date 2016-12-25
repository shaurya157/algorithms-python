def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []
    pivot = len(arr)/2
    for index, num in enumerate(arr):
        if index == pivot:
        	continue
        elif num <= arr[pivot]:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [arr[pivot]] + quick_sort(right)

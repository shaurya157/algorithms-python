def bsearch(arr, el):
	if len(arr) == 0:
		return None

	mid = len(arr)/2
	if arr[mid] == el:
		return mid
	elif arr[mid] > el:
		return bsearch(arr[0:mid], el)
	else:
		index = bsearch(arr[mid:], el)
		if index == None:
			return index
		else:
			return index + mid

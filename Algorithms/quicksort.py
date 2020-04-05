def quicksort(array: list) -> list:
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array if i < pivot]
		more = [i for i in array if i > pivot]
		return quicksort(less) + [pivot] + quicksort(more)


print(quicksort([3, 7, 2, 9, 11, 4, 8]))
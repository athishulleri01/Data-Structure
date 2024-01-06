# Selection Sort
# ...............
# Selection Sort has a time complexity of O(n^2). 
# In each iteration, the code finds the minimum element’s index in the unsorted portion of the array and swaps it with 
# the current index’s element. This gradually sorts the array from left to right. The example initializes an array, applies 
# the selectionSort function to sort it, and then prints the sorted array in ascending order. The sorted array is obtained 
# by repeatedly finding the smallest element in the unsorted portion and placing it in its correct position, resulting in an 
# ordered array: [-202, -97, -9, -2, 0, 11, 45, 88, 747].



# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)

# Insertion Sort
# .................
# The insertionSort function takes an array arr as input. It first calculates the length of the array (n). 
# If the length is 0 or 1, the function returns immediately as an array with 0 or 1 element is considered 
# already sorted.

# For arrays with more than one element, the function proceeds to iterate over the array starting from the second element.
# It takes the current element (referred to as the “key”) and compares it with the elements in the sorted portion of the array 
# that precede it. If the key is smaller than an element in the sorted portion, the function shifts that element to the right, 
# creating space for the key. This process continues until the correct position for the key is found, and it is then inserted in 
# that position.


def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
  
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
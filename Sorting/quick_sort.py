# # Quick sort in Python

# # function to find the partition position
# def partition(array, low, high):

#   # choose the rightmost element as pivot
#   pivot = array[high]

#   # pointer for greater element
#   i = low - 1

#   # traverse through all elements
#   # compare each element with pivot
#   for j in range(low, high):
#     if array[j] <= pivot:
#       # if element smaller than pivot is found
#       # swap it with the greater element pointed by i
#       i = i + 1

#       # swapping element at i with element at j
#       (array[i], array[j]) = (array[j], array[i])

#   # swap the pivot element with the greater element specified by i
#   (array[i + 1], array[high]) = (array[high], array[i + 1])

#   # return the position from where partition is done
#   return i + 1


# def partition(array,low,high):
#   pivot = array[low]
#   start = low
#   end = high
#   while start < end :
#     while array[start]<pivot:
#       start+=1
#     while array[end]<pivot:
#       end-=1
#     if start<end:
#       array[start],array[end]=array[end],array[start]
#   array[low],array[end] = array[end],array[low]
#   return end
      



# # function to perform quicksort
# def quickSort(array, low, high):
#   if low < high:

#     # find pivot element such that
#     # element smaller than pivot are on the left
#     # element greater than pivot are on the right
#     pi = partition(array, low, high)

#     # recursive call on the left of pivot
#     quickSort(array, low, pi - 1)

#     # recursive call on the right of pivot
#     quickSort(array, pi + 1, high)


# data = [8, 7, 2, 1, 0, 9, 6]
# print("Unsorted Array")
# print(data)

# size = len(data)

# quickSort(data, 0, size - 1)

# print('Sorted Array in Ascending Order:')
# print(data)



# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     pivot = array[len(array) // 2]
#     left = [x for x in array if x < pivot]
#     middle = [x for x in array if x == pivot]
#     right = [x for x in array if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)


# data = [8, 7, 2, 1, 0, 9, 6]
# print(data)

# data = quick_sort(data)
# print(data)

def partition(array, low, high):
    pivot = array[low]
    start = low + 1
    end = high
    while start <= end:
        while array[start] < pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start <= end:
            array[start], array[end] = array[end], array[start]

    array[low], array[end] = array[end], array[low]
    return end

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

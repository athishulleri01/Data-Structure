

def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    

arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = LinearSearch(arr,x)
print(result,arr[result])
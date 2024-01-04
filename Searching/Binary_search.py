def LinearSearch(arr,min,max,target):
    if max>=min:
        mid = ( max + min ) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid]< target:
            return LinearSearch(arr,mid+1,max,target)
        else:
            return LinearSearch(arr,min,mid-1,target)
    else:
        return -1
    

arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = LinearSearch(arr,0,len(arr)-1,x)
print(result,arr[result])
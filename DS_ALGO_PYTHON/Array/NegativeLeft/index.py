#sorted return a new array 



# arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]

# newArray  = sorted(arr)

# print(arr)
#  [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]
# print(newArray)

# [-7, -3, -1, 2, 4, 5, 6, 8, 9]


#  Dutch National Flag Algorithm
arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]
size = len(arr)
def traverseArray(arr,size):
    low=0
    mid=0
    high = size -1

    while mid<=high:
        if arr[mid]<0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low = low +1 
            mid = mid + 1
        else:
            mid = mid + 1
    return arr

newArr = traverseArray(arr,size)
print(newArr)

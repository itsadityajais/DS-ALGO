# c0=0 
# c1=0 
# c2=0
# arr = [0,1,1,0,2,0,2,1]
# sortArr=[]
    
# for item in arr:
#     if(item == 0):
#         c0 = c0 + 1
#     elif(item == 1):
#         c1 = c1 + 1
#     else:
#         c2 = c2 + 1
                
# i = 0
# while(c0 > 0):
#     # sortArr[i] = 0
#     sortArr.append(0)
#     i=i+1
#     c0 = c0 -1
# while(c1 > 0):
#     # sortArr[i] = 1
#     sortArr.append(1)
#     i=i+1
#     c1 = c1 -1
# while(c2 > 0):
#     # sortArr[i] = 2
#     sortArr.append(2)
#     i=i+1
#     c2 = c2 -1

# print(sortArr)
    



# Dutch National Flag problem
arr = [0,1,1,0,2,0,2,0]
size = len(arr)
def traverseArray(arr,size):
    low=0
    mid=0
    high = size -1

    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low = low +1 
            mid = mid + 1
        elif arr[mid]==1:
            mid = mid + 1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high = high - 1
        # print(low)
        # print(high)
        # print(mid)
        # print(arr)
    return arr

newArr = traverseArray(arr,size)
print(newArr)


# low=0
# high=7
# mid=0

# [0,1,1,0,2,0,2,0]
# arr[mid] = 0
#   swap -> [0,1,1,0,2,0,2,0]
#   increment low and mid by 1
 
# low=1
# high=7
# mid=1

# [0,1,1,0,2,0,2,0]
# arr[mid] = 1
#     increment mid by 1


# low=1
# high=7
# mid=2


# [0,1,1,0,2,0,2,0]
# arr[mid] = 1
#     increment mid by 1



# low=1
# high=7
# mid=3


# [0,1,1,0,2,0,2,0]
# arr[mid] = 0
#   swap -> [0,0,1,1,2,0,2,0]
#   increment low and mid by 1




# low=2
# high=7
# mid=4


# [0,0,1,1,2,0,2,0]
# arr[mid] = 2
#   swap -> [0,0,1,1,0,0,2,2]
#   decremnet high by 1



# low=2
# high=6
# mid=4

# [0,0,1,1,0,0,2,2]
# arr[mid] = 0
#   swap -> [0,0,0,1,1,0,2,2]
#   increment low and mid by 1



# low=3
# high=6
# mid=5

# [0,0,0,1,1,0,2,2]
# arr[mid] = 0
#   swap -> [0,0,0,0,1,1,2,2]
#   increment low and mid by 1


# low=4
# high=6
# mid=6

#    decremnet hight by 1

# low=4
# high=5
# mid=6

#     loop exit
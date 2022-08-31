# The range() function returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 (by default), 
# and stops before a specified number {VVI}.

# Syntax
# range(start, stop, step)
# Parameter Values
# Parameter	Description
# start	Optional. An integer number specifying at which position to start. Default is 0
# stop	Required. An integer number specifying at which position to stop (not included).
# step	Optional. An integer number specifying the incrementation. Default is 1


arr = [5,9,6,2,7,4,8,6,2]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print(arr)


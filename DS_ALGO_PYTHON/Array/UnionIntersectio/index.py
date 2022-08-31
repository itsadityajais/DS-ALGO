
# ____________________ UNION FOR SORTED ARRAYS ____________________
arr1 = [1,3,5,5,6,8,8,10]
arr2 = [2,4,4,7,9,11]

#merge both arrays

for num in arr2:
    arr1.append(num)


# remove duplicate
distinct1 = set(arr1)

print(distinct1)


# ____________________ INTERSECTION FOR SORTED ARRAYS ____________________

arr1 = [1,3,5,5,6,8,8,10,11]
arr2 = [2,4,4,5,7,9,11]
interArray = []

# remove duplicate
distinct1 = set(arr1)
distinct2 = set(arr2)

# Check if item is common btw both arrays

for numInDis1 in distinct1:
    for numInDis2 in distinct2:
        if numInDis1 == numInDis2:
            interArray.append(numInDis1)

print(interArray)
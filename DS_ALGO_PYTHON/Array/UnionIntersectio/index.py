
# ____________________ UNION FOR SORTED ARRAYS ____________________
# arr1 = [1,3,5,5,6,8,8,10]
# arr2 = [2,4,4,7,9,11]

# #merge both arrays

# for num in arr2:
#     arr1.append(num)


# # remove duplicate
# distinct1 = set(arr1)

# print(distinct1)


# ____________________ INTERSECTION FOR SORTED ARRAYS ____________________

# arr1 = [1,3,5,5,6,8,8,10,11]
# arr2 = [2,4,4,5,7,9,11]
# interArray = []

# # remove duplicate
# distinct1 = set(arr1)
# distinct2 = set(arr2)

# # Check if item is common btw both arrays

# for numInDis1 in distinct1:
#     for numInDis2 in distinct2:
#         if numInDis1 == numInDis2:
#             interArray.append(numInDis1)

# print(interArray)



#____________________ UNION FOR SORTED ARRAYS OPTIMAL ____________________

arr1 = [1,3,5,5,6,8,8,10]
arr2 = [2,4,4,7,9,11]
finalArr=[]

i=0
j=0

while i < len(arr1) and j < len(arr2):
    if arr1[i]<arr2[j]:
        finalArr.append(arr1[i])
        i=i+1
    elif arr1[i] > arr2 [j]:
        finalArr.append(arr2[j])
        j=j+1
    else:
        finalArr.append(arr2[j])
        j=j+1

if i < len(arr1):
    finalArr.append(arr1[i])
    i=i+1

if j < len(arr2):
    finalArr.append(arr2[j])
    j=j+1

print(finalArr)


# ____________________ INTERSECTION FOR SORTED ARRAYS OPTIMAL ____________________

arrFirst = [1,3,5,5,6,8,8,10]
arrSecond = [2,4,4,7,8,8,9,11]

arr1 = list(set(arrFirst))
arr2 = list(set(arrSecond))

finalArr=[]

i=0
j=0

while i < len(arr1) and j < len(arr2):
    if arr1[i]<arr2[j]:
        i=i+1
    elif arr1[i] > arr2 [j]:
        j=j+1
    else:
        finalArr.append(arr2[j])
        j=j+1
        i=i+1


print(finalArr)
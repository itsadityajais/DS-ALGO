# arr = [-2,3,-1,2]

# maxSum = -1000000000000
# currSum = 0

# for i in range(len(arr)):
#     currSum = 0
#     for j in range(i,len(arr)):
#         currSum=currSum+arr[j]
#         # print("currSum",currSum)
#         if(currSum>maxSum):
#             maxSum=currSum
# print(maxSum)

ar = [-2,3,-1,2]
n = len(ar)
maxSum = -1e8
currSum = 0

for i in range(n):
    currSum = currSum + ar[i]
    if currSum > maxSum:
        maxSum = currSum
    if currSum < 0:
        currSum = 0
print(maxSum)



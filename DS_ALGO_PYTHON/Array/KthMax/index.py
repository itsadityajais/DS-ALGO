arr = [6,7,2,645,3,78,9,3,8,3,6,8,54,]
k=2
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print(arr[k-1])


# import heapq
 
 
# def kthLargest(arr, size, k):
#     pq = []
 
#     for i in range(size):
#         heapq.heappush(pq, -1 * arr[i])
 
#     l = k - 1
#     while l > 0:
#         heapq.heappop(pq)
#         l = l - 1
 
#     return -1 * pq[0]
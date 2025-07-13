# You will be given a list of integers, arr, and a single integer k. You must sort the numbers in ascending order and create an array of length k from elements of arr to minimize its unfairness. Call that array arr’. Unfairness of an array is calculated as = max(arr’) – min(arr’)

# Where:- max denotes the largest integer in arr’- min denotes the smallest integer in arr’

# Input Format

# 1,11,25,98,66,53
# 4

# Constraints

# NA

# Output Format

# 1 11 25 53

# Sample Input 0

# 1,4,7,2
# 2
# Sample Output 0

# 1 2
# Sample Input 1

# 2,7,6,11,13
# 3
# Sample Output 1

# 2 6 7

array=list(map(int,input().split(',')))
k=int(input())

array.sort()
min_val=float('inf')
res=[]

for i in range(len(array)-k+1):
    arr=array[i:i+k]
    # print("f", arr)
    unf=arr[k-1]-arr[0]
    # print(unf,min_val)
    min_val=min(min_val, unf)
    # print(unf,min_val)
    if unf<=min_val:
        # print("res=",arr)
        res=arr
        
for j in range(len(array),len(array)-k,-1):
    arr=array[j-k:j]
    # print("b", arr)
    if arr==[]:
        break
    unf=arr[k-1]-arr[0]
    min_val=min(min_val, unf)
    if unf<=min_val:
        res=arr
# print(min_val)
# print(res)

for i in res:
    print(i, end=' ')

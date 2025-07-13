from collections import deque
n,k=map(int,input().split())
kicks=list(map(int,input().split()))

max_k=0
# result=[]
result=deque()

for i in range(n):
    if kicks[i]<max_k:
        kicks.pop(i)
    else:    
        max_k=max(kicks[i:k+i])
    result.append(max_k)
# for i in range(n):



# for r in result:
#     print(r, end=' ')
print(result)
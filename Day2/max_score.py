n,k=map(int,input().split())
ts=list(map(int,input().split()))

max_t=0
for i in range(n-k+1):
    # print(ts[i:k+i], sum(ts[i:k+i]))
    max_t=max(sum(ts[i:k+i]),max_t)
print(max_t)
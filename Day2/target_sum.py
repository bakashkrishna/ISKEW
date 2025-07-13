n=int(input())
arr=list(map(int,input().split()))
target=int(input())

for i in (arr):
    k=target-i
    arr.remove(i)
    if k in arr:
        print("Yes")
        break
    arr.append(i)
else:
    print("No")

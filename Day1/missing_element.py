n=int(input("Enter n: "))
arr=set(map(int,input("Enter the the array: ").split()))

# nums=set(range(0,n))
# print(nums-arr)


esum=n*(n+1)//2
asum=sum(arr)
print(esum-asum)
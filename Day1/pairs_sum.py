arr=list(map(int,input("Enter the the array: ").split()))

k=int(input("Enter the target: "))

pairs=[]

for i in set(arr):
    if k+i in arr:
        if k+i==i and arr.count(i)<2:
            continue
        pairs.append((i,k+i))

print("The pairs are: ",pairs)
print("The count of pairs are: ",len(pairs))
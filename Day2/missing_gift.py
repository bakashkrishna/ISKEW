n=int(input())
gifts=set(map(int,input().split()))
found=set(map(int,input().split()))

print(gifts - found)
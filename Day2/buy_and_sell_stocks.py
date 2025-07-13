prices=list(map(int,input().split(',')))
min_p=prices[0]
max_profit=0
profit=0
for p in prices:
    min_p=min(min_p,p)
    if p>min_p:
        profit+=p-min_p
        min_p=p
    max_profit=max(max_profit,profit)
print(max_profit)
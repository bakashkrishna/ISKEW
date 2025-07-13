s=input()

count=0
chair=0
for c in s:
    if c=='C' or c=='U':
        if(count):
            count-=1
        else:
            chair+=1
        # if count==0:
        #     chair+=1
    elif c=='R' or c=='L':
        count+=1
    else:
        continue
print(chair)
# The postal service in Kothamangalam is interested in cutting costs as an alternative to raising postage rates. One effective way to do this is by minimizing the distance traveled by the delivery truck when delivering mail from the post office to all required locations and returning.

# The truck may not be able to carry all the mail at once, so it might need to return to the post office multiple times to reload. For simplicity, assume that all delivery locations are arranged on a one-dimensional number line, with the post office located at coordinate 0. Each delivery location is identified by a single non-zero coordinate.

# Example

# Suppose the truck can carry up to 100 letters. Letters need to be delivered to the following locations:

# 50 letters to location -10
# 175 letters to location 10
# 20 letters to location 25
# An efficient delivery plan would be:

# Trip 1: Deliver 50 letters to -10 → round trip: 2 × 10
# Trip 2: Deliver 100 letters to 10 → round trip: 2 × 10
# Trip 3: Deliver remaining 75 letters to 10 and 20 letters to 25 (on the same trip) → round trip: 2 × 25
# Total Distance = (2 × 10) + (2 × 10) + (2 × 25) = 90

# Input

# The first line contains two integers, N and K, where N is the number of delivery addresses on the route, and K is the carrying capacity of the postal truck. Each of the following lines will contain two integers xi and ti, the location of a delivery and the number of letters to deliver there, where, for all i:

# xi — the coordinate of a delivery location (-1500 ≤ xi ≤ 1500, xi ≠ 0)
# 1 <= ti <= 800
# All delivery locations are nonzero (that is, none are at the post office).
# Output

# Output the minimum total travel distance needed to deliver all the letters and return to the post office.

# Input Format

# 3 100 -10 50 10 175 25 20

# Constraints

# NA

# Output Format

# 90

# Sample Input 0

# 3 100
# -10 50
# 10 175
# 25 20
# Sample Output 0

# 90

locs,limit=map(int,input().split())
dist=[]
for i in range(locs):
    dist.append(list(map(int,input().split())))
# print(locs,limit,dist)
dist=dist[::-1]
cap=0
cost=0
for i in dist:
    # print(i,i[1])
    if cap<=limit:
        # print(i[1],limit,cap)
        if i[1]<=limit-cap:
            # print(cap)
            cap+=i[1]
            # print(cap)
            # print(i[1])
            i[1]=0
            # print(i[1])
        else:
            while(i[1]!=0):
                # print("l,c",limit,cap)
                if cap==limit:
                    cap=0
                if limit>=i[1]:
                    cap=i[1]
                    i[1]=0
                else:
                    i[1]-=limit-cap
                    # print("cap",cap)
                    # print("i",i[1])
            
    if i[1]==0:
        # print("cost",cost)
        # print("i[0]",i[0])
        cost+=abs(i[0])*2
        # print("cost",cost)
    # print("capa",cap)
print(cost)
        
        
        
    
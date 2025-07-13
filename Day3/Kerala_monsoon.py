# Kerala, blessed with the Western Ghats and abundant monsoon rains, also witnesses a high number of lightning strikes every year, especially during the pre-monsoon and monsoon seasons. On average, districts like Idukki and Wayanad can record intense lightning activity due to their elevation and cloud dynamics.

# Appu, a young engineer from Kothamangalam, is designing lightning protection for a row of buildings in a hilly town in Kerala. He surveys N buildings arranged from west to east along a narrow road winding through the hills. The peak of building i has coordinates (Xi, Yi), where Xi is the horizontal distance from the western end and Yi is the height from sea level (in meters).

# Appu wants to place lightning rods on top of some buildings. A rod on a building protects that building and all buildings that lie on or under the 45° line of depression both westward and eastward.

# In mathematical terms, a lightning rod on building i protects building j if and only if |Xi − Xj| ≤ Yi − Yj.

# Your task is to help Appu determine the minimum number of lightning rods he needs to install to protect all the buildings in the street.

# Input Format

# Your program must read from standard input.

# The first line contains a single integer N, the number of buildings.
# The next N lines contain two integers Xi and Yi, describing the position and height of the buildings.
# The Xi values are guaranteed to be in increasing order (i.e., Xi ≤ Xi+1).
# Output Format

# Print a single integer: the minimum number of lightning rods needed to protect all buildings.

# Input Format

# 5
# 1 3
# 2 2
# 3 1
# 5 2
# 6 1

# Constraints

# NA

# Output Format

# 2

# Sample Input 0

# 5
# 1 3
# 2 2
# 3 1
# 5 2
# 6 1
# Sample Output 0

# 2


n=int(input())
cords={}
for i in range(n):
    x,y=(map(int,input().split()))
    if y in cords:
        cords[y].append(x)
    else:
        cords[y]=[x]

# print(n,cords)

Y=[]
for c in cords.keys():
    Y.append(c)
Y.sort(reverse=True)
# print(Y)

i=0
j=len(Y)-1
count=len(Y)
while(i<j):
    # print(cords[Y[i]])
    if Y[i]-Y[j] >= cords[Y[i]][0]-cords[Y[j]][0]:
        i+=1
        j-=1
        count-=1
    else:
        i+=1
        j-=1
print(count)




# from collections import deque

# n=int(input())
# cords=[]
# for i in range(n):
#     cordinate=list((map(int,input().split())))
#     cords.append(cordinate)

# towers=deque()
# i=0
# while i<len(cords):
#     print(cords[i],cords[i+1])
#     print(cords[i][1], "-", cords[i+1][1], ">=", cords[i][0], "-", cords[i+1][0])
#     y_diff=abs(cords[i][1]-cords[i+1][1])
#     x_diff=abs(cords[i][0]-cords[i+1][0])
#     if y_diff >= x_diff:
#         res=[x_diff,y_diff]
#         towers.append(res)
#         i+=1
#     else:
#         i-=1
#         continue
#     # else:
#     #     towers.append(cords[i])
# print(towers)
# print(len(towers))
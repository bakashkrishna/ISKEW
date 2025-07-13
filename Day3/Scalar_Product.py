# You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The scalar product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.

# Suppose you are allowed to permute the coordinates of each vector as you wish. Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product.

# Input

# For each test case, the first line contains integer number n. The next two lines contain n integers each, giving the coordinates of v1 and v2 respectively.

# Output

# For each test case, output a single number Y, which is the minimum scalar product of all permutations of the two given vectors.

# Input Format

# 3
# 1 3 -5
# -2 4 1

# Constraints

# NA

# Output Format

# -25


# Output explanation:

# (-5 * 4) + (-2 * 3) + (1 * 1) = (-20) + (-6) + 1 = -25

# Sample Input 0

# 3
# 1 3 -5
# -2 4 1
# Sample Output 0

# -25

n=int(input())
v1=list(map(int,input().split()))
v2=list(map(int,input().split()))

v1.sort()
v2.sort(reverse=True)

sumv=0
for i in range(n):
    sumv+=v1[i]*v2[i]
    
print(sumv)
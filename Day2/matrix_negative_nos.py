n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

i = 0         
j = m - 1      
count = 0

while i < n and j >= 0:
    if matrix[i][j] < 0:
        # All elements in this row before column j are also negative
        count += (j + 1)
        i += 1
    else:
        j -= 1

print(count)

    
m,n=map(int,input().split())
a=[]
b=[]

def read(x,n):
    for _ in range(n):
        row=list(map(int,input().split()))
        x.append(row)
    
def display(x):
    for i in range(m):
        for j in range(n):
            print(x[i][j], end=' ')
        print()
    
def add(a, b):
    s = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(a[i][j] + b[i][j])
        s.append(row)
    return s
     
read(a,n)
read(b,n)

print("First Matrix: ")
display(a)
print("Second Matrix: ")
display(b)
print("Sum of the two matrices is: ")
s = add(a, b)
display(s)

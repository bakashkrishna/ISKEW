n=int(input())
minstack=[]

def push(X): 
    # push X into the stack.
    minstack.append(X)
    
def pop(): 
    # remove the top element from the stack.
    if(minstack):
        minstack.pop()
    
    
def top(): 
    # returns (but not remove) the top element on the stack.
    if minstack:
        return minstack[-1]
    return None

def getMin(): 
    # returns (but not remove) the minimum element on the stack.
    if minstack:
        return min(minstack)
    return None

for _ in range(n):
    inp=input().strip().split()
    op=int(inp[0])
    if op==0:
        val=int(inp[1])
        push(val)
    elif op==1:
        pop()
    elif op==2:
        print(top())
    elif op==3:
        print(getMin())
    else:
        print("Invalid input")

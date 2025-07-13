s=input()
stack=[]
def ismatch(s):
    for i in s:
        if i=='{':
            stack.append(i)
        else:
            if(stack):
                stack.pop()
            else:
                print("Not Matching")
                return
    if(stack):
        print("Not Matching")
    else:
        print("Matching")
ismatch(s)
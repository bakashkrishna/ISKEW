n=int(input("Enter the nth day: "))

f=n%5
if f==1:
    print("Thumb")
elif f==2:
    print("Index")
elif f==3:
    print("Middle")
elif f==4:
    print("Ring")
elif f==0:
    print("Pinky")
else:
    print("Invalid input")
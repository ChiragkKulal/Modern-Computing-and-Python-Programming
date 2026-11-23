positive=0
negative=0
while True:
    n=int(input("enter a number:"))
    if n==-1:
        break
    elif n>0:
        print("positive number")
        positive=positive+n
    elif n<0:
             print("negative number")
             negative=negative+n   
    else:
        print("zero")
print("total positive number =",positive)
print("total negative number =",negative)
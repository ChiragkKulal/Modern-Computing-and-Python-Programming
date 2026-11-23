psum=0
nsum=0
zerocount=0

number=int(input("enter a number"))

while number!=-1:
    if number>0:
        psum=psum+number
    elif number<0:
        nsum=nsum+number
    else:
        zerocount=zerocount+1

    number=int(input("enter a number:"))
    
print(f"sum of all positive number {psum}")
print(f"sum of all negative number {nsum}")
print(f"sum of all zeros {zerocount}")
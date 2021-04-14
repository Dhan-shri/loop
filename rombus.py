n=int(input("enter a number"))
i=1
while n>0:
    b=1
    while b<n:
        print("   ",end="")
        b=b+1
    k=1
    while k<=i:
        print(" * ",end="")
        k=k+1
    print()
    i=i+1
    n=n-1
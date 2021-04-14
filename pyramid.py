n=int(input(("enter a number of rows")))
i=1
while i<=n:
    space=n-i
    j=1
    while j<=space:
        print(" ",end="")
        j=j+1
    stars= 2*i-1
    while stars>0:
        print("*", end="")
        stars= stars-1
    print()
    i=i+1
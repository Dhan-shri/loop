n=int(input("enter a number of rows"))
i=1
while n>0:
    b=1
    while b<i:
        print(" ",end="")
        b=b+1
    star=1
    while star<=(n*2)-1:
        print("*",end="")
        star=star+1
    print()
    n=n-1
    i=i+1
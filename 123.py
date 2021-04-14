# n=int(input("enter a number of rows"))
# i=1
# while (i<=n):
#     j = 1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1

n=int(input("enter a number of rows"))
i=1
while n>0:
    s=1
    while s<n:
        print("  ",end="")
        s=s+1
    num=1
    while num<=i:
        print(num," ", end="")
        num=num+1
    print()
    i=i+1
    n=n-1
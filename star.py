# i=1
# while i<=3:
#     print("* " *i)
#     i=i+1

# i=3
# while i>=1:
#     print("* "*i)
#     i=i-1

# i = 1
# while(i <= 4):
#     j = 1
#     while(j <= 4):
#         if(j <= 4 - i):
#             print(' ', end = '  ')
#         else:
#             print('*', end = '  ')
#         j = j + 1
#     i = i + 1
#     print()


i=1
while i<=3:
    j=1
    while j<=3:
        if j<=i:
            print(" * ",end="")
        else:
            print(" ",end="")
        j=j+1
    print()
    i=i+1

# n=int(input("enter a number of rows"))
# i=1
# while n>0:
#     j=1
#     while j<=n:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1
#     n=n-1
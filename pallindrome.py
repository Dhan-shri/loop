num=int(input("enter a number"))
ori=num
i=1
rev=0
rem=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
    i=i+1
if ori==rev:
    print("it is pallindrome number")
else:
    print("it is not pallindrome number")

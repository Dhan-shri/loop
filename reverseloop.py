n=int(input("enter a number"))
rev=0
rem=0
i=1
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
    i=i+1
print(rev)
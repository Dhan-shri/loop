#number whose sum of the factorial of digits is equal to the original number. 
num=int(input("Enter a number:"))
sum=0
b=num
while(num):
    i=1
    f=1
    r=num %10
    while(i<=r):
        f=f*i
        i=i+1
    sum=sum+f
    num=num//10
if(sum==b):
    print("The number is a strong number")
else:
    print("The number is not a strong number")
num=int(input("enter a number"))
a=num
sum=0
count=1
while num>0:
    sum=sum+(num%10)*(num%10)*(num%10)*(num%10)
    count=count+1
    num=num//10
if a==sum:
    print("it is amstrong number")
else:
    print("it is not a amstrong number")
i=1
sum=0
avg=0
while i<=11:
    weight=int(input("enter a weight"))
    sum=sum+weight
    avg=sum/11
    i=i+1
print(avg)
if avg%5==0:
    print("avg 5 se divisible hai")
else:
    print("divisibl nahi hai5")

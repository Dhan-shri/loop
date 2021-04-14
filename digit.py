n=int(input("enter any number"))
count=0
while n>1:
    count=count+1
    n=n//10
print( "number of digit is",count)
i = 1
sum = 0
n=int(input("enter a number"))
while(i <=n) :
    if (n % i == 0) :
        sum += i
        print(i)
    i += 1
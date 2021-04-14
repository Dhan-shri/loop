
# a positive integer that is equal to the sum of its positive divisors, excluding the number itself. 
i = 1
sum = 0
n = int(input("Enter a number: "))
while(i <= n /2 ) :
    if (n % i == 0) :
        sum=sum+ i
    i =i+ 1
if sum == n :
    print(n,"is a perfect number")
else :
    print(n,"is not a perfect number")
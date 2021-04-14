a=5
print("you are guessing is 1 to 10 numbers")
i=1
while i<=10:
    num=int(input("enter any number "))
    if a>num:
        print("aapka number chota hai. phir se try kare")
    if a<num:
        print("aapka number bada hai. phir se try kare")
    if a==num:
        print("aapka guess barabar hai")
        break
    i = i+1
if i>5:
    print("your chances are complete")
    
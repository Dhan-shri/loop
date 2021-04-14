# name=input("enter your name")
# total=0
# i=1
# while i<=len(name):
#     total=total+1
#     i=i+1
# print(total)

# string = input("Enter a string")
# acc = ""
# for char in string:
#     if char == " ":
#         char = "_"
#     acc += char
# print(acc)

# string= "komal"
# string1=string.upper()
# print(string1)

# name=input("enter a name")
# a=name
# i=0
# while (i<=len(name)):
#     print(name.upper(),"" ,  end="")
# i=0
# x="komal"
# while i<len(x) :
#     print(x.upper()[0],"_",end=" ")
#     print(x.upper()[1], x.lower()[1],"_",end="")
#     print(x.upper()[2],x.lower()[2], x.lower()[2],"_",end="")
#     i=i+1   



x=input("enter a name")
i=0
while i<len(x):
    print(x.upper()[i]+i*(x[i]),end="")
    if i!=len(x)-1:
      print("_",end="")
    i=i+1

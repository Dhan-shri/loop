# # value patterns of stars 65
# inc = 1
# for i in range(0, 5):
# for j in range(0, inc):
# ch = chr(value)
# print(ch, end=" ")
# value = value + 1
# inc = inc + 2
# print()

# num=int(input("enter a number"))


# a=[1,2,2,2,2,3,6]
# i=0
# # count=0
# while i<len(a):
#     j=0
#     k=0
#     while j<len(a):
#         if a[i]==a[j]:
#             k=k+1
#         j=j+1
#     i=i+1
# print(k)   

a=[1,2,4,4,2,4]
i=0
k=[]
while i<len(a):
    num=a[i]
    j=0
    while j<len(a):
        if num in a:
            k.append(num)
        j=j+1
    i=i+1
print(k)

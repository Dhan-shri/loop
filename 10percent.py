quantity=int(input("enter a quantity"))
if quantity>=1000:
    print("the total cost after discount is",quantity-quantity*10/100)
else:
    print("the cost remain same")
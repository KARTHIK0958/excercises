quantity=int(input("enter the quantity :"))
price=int(input("enter the price : Rs."))
def exp(quantity,price):
    if quantity>10:
        discount=(price*quantity)*0.1
        total=print("Total Price Will be : Rs.",(price*quantity)-discount,"/-")
    else:
        total=print("Total Price Will be : Rs.",price*quantity,"/-")
    return total
exp(quantity,price)
    
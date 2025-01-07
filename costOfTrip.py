km=int(input("enter the kilometers to drive :"))
kmph=int(input("enter the Kilometers-per-litre usage of the car :"))
FPL=int(input("enter the price per liter of fuel :"))
def costOfTrip():
    fuelConsumed=int(km/kmph)
    cost=fuelConsumed*FPL
    print("Total Cost of the trip will be",cost)
costOfTrip()
    
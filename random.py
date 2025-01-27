import random
def rand():
    return (random.randint(1,10))
ln=int(input("Enter the lucky number between 1 to 10 :"))
if ln not in range(1,10):
    print("Enter the lucky number between 1 to 10 :")
while True:
    random_number=rand()
    if ln==random_number:
        print("Generated random number ",random_number," is equal to the lucky number ",ln)
        break;
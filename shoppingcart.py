def shopping_cart():
    items = [
        ['Bread', 40],
        ['Cookies', 80],
        ['Butter', 120],
        ['Cheese', 180],
        ['Yoghurt', 60]
    ]
    cart = []

    while 1:
        print("\nWhat do you want to do?")
        print("1. View items")
        print("2. Add items to cart")
        print("3. Update items in cart")
        print("4. Delete items from cart")
        print("5. Print bill")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"1. Bread =40")
            print(f"2. Cookies=80")        
            print(f"3. Butter=120") 
            print(f"4. Cheese=180")  
            print(f"5. Yoghurt=60")

        elif choice == '2':
            item_name = input("Enter the item name: ")
            for item in items:
                if item[0] == item_name:
                    quantity = int(input("Enter the quantity: "))
                    for cart_item in cart:
                        if cart_item[0] == item_name:
                            cart_item[1] += quantity
                            break
                    else:
                        cart.append([item_name, quantity])
                    break
            else:
                print("Invalid item.")
        elif choice == '3':
            item_name = input("Which item to be updated: ")
            for cart_item in cart:
                if cart_item[0] == item_name:
                    quantity = int(input("Enter the new quantity: "))
                    cart_item[1] = quantity
                    print(f"Quantity of {item_name} updated to {quantity}")
                    break
            else:
                print("Item not found in cart.")
        elif choice == '4':
            item_name = input("Which item to be removed: ")
            for cart_item in cart:
                if cart_item[0] == item_name:
                    cart.remove(cart_item)
                    print(f"{item_name} removed from the cart")
                    break
            else:
                print("Item not found in cart.")
        elif choice == '5':
            print("\nCart items:")
            print("Name, Quantity, Price, Total")
            total_amount = 0
            for cart_item in cart:
                for item in items:
                    if item[0] == cart_item[0]:
                        price = item[1]
                        total = price * cart_item[1]
                        total_amount += total
                        print(f"{cart_item[0]}, {cart_item[1]}, {price}, {total}")
                        break
            print(f"Total Bill: {total_amount}")
        elif choice == '6':
            print("Thank You for Shopping !")
            break

        print("Invalid choice. Please try again.")
shopping_cart()
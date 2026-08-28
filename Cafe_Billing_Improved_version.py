cafe_menu = {
    "Espresso": {"Price": 120, "Category": "Beverages"},
    "Cappuccino": {"Price": 150, "Category": "Beverages"},
    "Cheese Burger": {"Price": 180, "Category": "Snacks"},
    "French Fries": {"Price": 90, "Category": "Snacks"},
    "Choco Lava Cake": {"Price": 140, "Category": "Desserts"}
}

customer_cart = {}


# ==================== DISPLAY MENU ====================

def menu():
    print("\n" + "=" * 55)
    print("                    CAFE MENU")
    print("=" * 55)

    print(f"{'Item':<22}{'Price':<10}{'Category'}")
    print("-" * 55)

    for item, details in cafe_menu.items():
        print(f"{item:<22}₹{details['Price']:<9}{details['Category']}")

    print("=" * 55)
    print("You will not be disappointed after placing an order with us!\n")


# ==================== PLACE ORDER ====================

def order():
    while True:
        menu()

        item = input("Enter item (or 'Done' to finish): ").strip()

        if item.lower() == "done":
            print("\nOrder completed successfully!")
            break

        if item not in cafe_menu:
            print("Item not available. Please select an item from the menu.")
            continue

        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")

        if item in customer_cart:
            customer_cart[item] += quantity
        else:
            customer_cart[item] = quantity

        print(f"{item} x {quantity} added successfully!")


# ==================== SHOW CART ====================

def show_cart():
    if not customer_cart:
        print("\nYour cart is empty.")
        return

    print("\n" + "=" * 65)
    print("                         YOUR CART")
    print("=" * 65)

    print(f"{'Item':<22}{'Price':<10}{'Qty':<10}{'Subtotal'}")
    print("-" * 65)

    total = 0

    for item, quantity in customer_cart.items():
        price = cafe_menu[item]["Price"]
        subtotal = price * quantity
        total += subtotal

        print(f"{item:<22}₹{price:<9}{quantity:<8}₹{subtotal}")

    print("-" * 65)
    print(f"{'Cart Total':>52} ₹{total}")
    print("=" * 65)


# ==================== REMOVE ITEM ====================

def remove_item():
    if not customer_cart:
        print("\nYour cart is empty.")
        return

    show_cart()

    item = input("\nEnter item to remove: ").strip()

    if item not in customer_cart:
        print("This item is not in your cart.")
        return

    del customer_cart[item]

    print(f"{item} removed successfully.")


# ==================== BILLING ====================

def billing():
    if not customer_cart:
        print("\nYour cart is empty. Please place an order first.")
        return

    subtotal = 0

    print("\n" + "=" * 65)
    print("                     THE COFFEE CORNER")
    print("                         FINAL BILL")
    print("=" * 65)

    print(f"{'Item':<22}{'Price':<10}{'Qty':<8}{'Amount'}")
    print("-" * 65)

    for item, quantity in customer_cart.items():
        price = cafe_menu[item]["Price"]
        amount = price * quantity
        subtotal += amount

        print(f"{item:<22}₹{price:<9}{quantity:<8}₹{amount}")

    print("-" * 65)
    print(f"{'Subtotal':>52} ₹{subtotal:.2f}")

    # ==================== DISCOUNT ====================

    coupon = input("\nEnter coupon code (or press Enter to skip): ").strip().upper()

    if coupon == "CAFE10":
        discount = subtotal * 0.10
        print("Coupon Applied: 10% OFF")
        
    elif coupon == "CAFE20":
        discount = subtotal * 0.20
        print("Coupon Applied: 20% OFF")

    elif coupon == "":
        discount = 0
        print("No coupon applied.")

    else:
        discount = 0
        print("Invalid coupon code.")

    final_total = subtotal - discount

    print("-" * 65)
    print(f"{'Discount':>52} ₹{discount:.2f}")
    print(f"{'Final Total':>52} ₹{final_total:.2f}")
    print("=" * 65)

    print("\nThank you for visiting The Coffee Corner!")
    print("Please collect your order from the counter.\n")


# ==================== MAIN MENU ====================

while True:

    print("\n" + "=" * 55)
    print("              WELCOME TO THE COFFEE CORNER")
    print("=" * 55)

    print("1. View Cafe Menu")
    print("2. Place Order")
    print("3. Show Cart")
    print("4. Remove Item")
    print("5. Generate Bill")
    print("6. Exit")

    print("=" * 55)

    option = input("Enter your option: ").strip()

    if option == "1":
        menu()

    elif option == "2":
        order()

    elif option == "3":
        show_cart()

    elif option == "4":
        remove_item()

    elif option == "5":
        billing()

    elif option == "6":
        print("\nThank you for visiting The Coffee Corner!")
        print("Exiting...")
        break

    else:
        print("\nInvalid option. Please select between 1 and 6.")

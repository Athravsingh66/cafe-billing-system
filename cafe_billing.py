cafe_menu = {
    "Espresso": {"Price": 120, "Category": "Beverages"},
    "Cappuccino": {"Price": 150, "Category": "Beverages"},
    "Cheese Burger": {"Price": 180, "Category": "Snacks"},
    "French Fries": {"Price": 90, "Category": "Snacks"},
    "Choco Lava Cake": {"Price": 140, "Category": "Desserts"}
}


# Display Cafe Menu to Customer

def menu():
    print("\n============================== Cafe Menu ==============================\n")

    for item, details in cafe_menu.items():
        print(item, "-", details["Price"], "-", details["Category"])

    print("\nYou will not be disappointed after placing an order with us!\n")


# Add Items to Customer Cart

customer_cart = []


def order():
    while True:

        print("\n============================== Cafe Menu ==============================\n")

        for item, details in cafe_menu.items():
            print(item, "-", details["Price"], "-", details["Category"])

        item = input("\nEnter your order (or type 'Done' to finish): ").strip()

        if item in cafe_menu:
            customer_cart.append(item)
            print(item, "added successfully!\n")

        elif item.lower() == "done":
            break

        else:
            print("Item not available. Please choose an item from the menu.\n")

    print("Your orders are:", customer_cart)


# Calculate Customer Bill

def billing():
    total = 0

    print("\n============================== Bill ==============================\n")

    for item in customer_cart:
        price = cafe_menu[item]["Price"]
        print(item, "-", price)
        total += price

    print("\n==================================================================")
    print("Your total bill is:", total)

    print("\nPlease go to the counter to collect your order.\n")


# Main Menu

while True:

    print("\n====================== Welcome to The Coffee Corner ======================\n")
    print("Please select an option:\n")
    print("1. Cafe Menu")
    print("2. Place Order")
    print("3. Show Cart")
    print("4. Billing")
    print("5. Exit")

    option = input("\nEnter your option: ").strip()

    if option == "1":
        menu()

    elif option == "2":
        order()

    elif option == "3":
        print("Your orders are:", customer_cart)

    elif option == "4":
        billing()

    elif option == "5":
        print("\nThank you for visiting The Coffee Corner!")
        print("Exiting...\n")
        break

    else:
        print("Invalid input. Please select an option from 1 to 5.")

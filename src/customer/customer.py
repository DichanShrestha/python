MENU_FILE = "src/data/menu.txt"
ORDERS_FILE = "src/data/orders.txt"

def extract_menu():
    menu = []
    try:
        with open(MENU_FILE, "r") as f:
            for line in f:
                category, name, price = line.strip().split(',')
                menu.append((category, name, price))
    except FileNotFoundError:
        print("Menu file not found.")
    return menu

def view_menu():
    print("\n--- Restaurant Menu ---")
    menu = extract_menu()
    if menu:
        for category, name, price in menu:
            print(category + " | " + name + " | Rs" + price)
    else:
        print("Menu unavailable.")

def place_order():
    print("\n--- Place Order ---")
    username = input("Enter username: ")
    view_menu()
    order_items = []
    total = 0
    menu = extract_menu()
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        found = False
        for category, name, price in menu:
            if item_name.lower() == name.lower():
                order_items.append(name + ":" + price)
                total += float(price)
                found = True
                break
        if not found:
            print("Item not found in menu.")
    if order_items:
        with open(ORDERS_FILE, "a") as f:
            order_id = "20250325123045"
            order_data = order_id + "," + username + "," + ",".join(order_items) + ",Total:" + str(total) + ",Pending\n"
            f.write(order_data)
        print("Order placed! Order ID: " + order_id)
        print("Total: Rs" + str(total))

def view_order_status():
    print("\n--- Order Status ---")
    username = input("Enter username: ")
    try:
        with open(ORDERS_FILE, "r") as f:
            user_orders = [order.strip().split(',') for order in f if username in order]
        if not user_orders:
            print("No orders found.")
            return
        for order in user_orders:
            print("\nOrder ID: " + order[0])
            for item in order[2:-2]:
                name, price = item.split(':')
                print("- " + name + ": Rs" + price)
            print("Total: " + order[-2])
            print("Status: " + order[-1])
    except FileNotFoundError:
        print("No orders found.")

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Order Status")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")
        if choice == '1':
            view_menu()
        elif choice == '2':
            place_order()
        elif choice == '3':
            view_order_status()
        elif choice == '4':
            print("Thank you!")
            break
        else:
            print("Invalid choice.")


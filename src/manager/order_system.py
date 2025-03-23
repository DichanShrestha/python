from datetime import datetime

# File paths for persistent storage
MENU_FILE = "src/data/menu.txt"
ORDERS_FILE = "src/data/orders.txt"

def initialize_data():
    """Initialize menu and orders from files or create defaults if files don't exist."""
    global menu, orders
    
    # Initialize menu from file or with defaults
    try:
        menu = {}
        with open(MENU_FILE, 'r') as file:
            for line in file:
                if line.strip():
                    item, price = line.strip().split(':', 1)
                    menu[item] = float(price)
    except FileNotFoundError:
        menu = {
            "Momo": 220,
            "Keema Noodles": 200,
            "Samosa Chhaat": 120,
            "Coke": 50
        }
        save_menu()
    
    # Initialize orders from file or with empty list
    orders = []
    try:
        with open(ORDERS_FILE, 'r') as file:
            current_order = None
            for line in file:
                line = line.strip()
                if line.startswith("ORDER_ID:"):
                    if current_order:
                        orders.append(current_order)
                    order_id = int(line.split(':', 1)[1])
                    current_order = {"order_id": order_id, "items": []}
                elif line.startswith("CUSTOMER:"):
                    current_order["customer"] = line.split(':', 1)[1]
                elif line.startswith("DATETIME:"):
                    current_order["datetime"] = line.split(':', 1)[1]
                elif line.startswith("ITEM:"):
                    current_order["items"].append(line.split(':', 1)[1])
                elif line.startswith("TOTAL:"):
                    current_order["total"] = float(line.split(':', 1)[1])
            if current_order:
                orders.append(current_order)
    except FileNotFoundError:
        save_orders()

def save_menu():
    """Save menu to file."""
    with open(MENU_FILE, 'w') as file:
        for item, price in menu.items():
            file.write(f"{item}:{price}\n")

def save_orders():
    """Save orders to file."""
    with open(ORDERS_FILE, 'w') as file:
        for order in orders:
            file.write(f"ORDER_ID:{order['order_id']}\n")
            file.write(f"CUSTOMER:{order['customer']}\n")
            file.write(f"DATETIME:{order['datetime']}\n")
            for item in order['items']:
                file.write(f"ITEM:{item}\n")
            file.write(f"TOTAL:{order['total']}\n")
            file.write("\n")  # Empty line to separate orders

def show_menu():
    """Displays the available menu items with prices."""
    print("\n=== MENU ===")
    print("-" * 20)
    for idx, (item, price) in enumerate(menu.items(), 1):
        print(f"{idx}. {item:<15} Rs{price:>4}")
    print("-" * 20)

def validate_customer_name():
    """Validates that customer name is not empty."""
    while True:
        name = input("\nEnter customer name: ").strip()
        if name:
            return name
        print("Error: Customer name cannot be empty!")

def get_menu_item_by_number(number):
    """Converts menu item number to item name."""
    try:
        idx = int(number) - 1
        if 0 <= idx < len(menu):
            return list(menu.keys())[idx]
    except ValueError:
        pass
    return None

def take_order():
    """Takes an order from the customer and stores it in the orders list."""
    customer_name = validate_customer_name()
    order_items = []
    
    print("\nEnter item number or name (or 'done' to finish)")
    show_menu()
    
    while True:
        item = input("Add item: ").strip()
        if item.lower() == 'done':
            break
            
        menu_item = get_menu_item_by_number(item)
        if menu_item:
            order_items.append(menu_item)
            print(f"Added {menu_item} to order")
        elif item in menu:
            order_items.append(item)
            print(f"Added {item} to order")
        else:
            print(f"Error: '{item}' is not available. Please try again.")
            print("Available items:")
            show_menu()

    if order_items:
        # Generate a new order ID (highest existing ID + 1)
        order_id = 1
        if orders:
            order_id = max([order.get('order_id', 0) for order in orders]) + 1
        
        order = {
            "order_id": order_id,
            "customer": customer_name,
            "items": order_items,
            "total": sum(menu[item] for item in order_items),
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        orders.append(order)
        save_orders()  # Save orders to file after adding new order
        print(f"\nOrder placed successfully!")
        print_order(order)
    else:
        print("\nNo valid items ordered. Order not placed.")

def print_order(order):
    """Prints a single order in a formatted way."""
    try:
        print("\n" + "-" * 40)
        print(f"Order ID: #{order['order_id']}")
        print(f"Date: {order['datetime']}")
        print(f"Customer: {order['customer']}")
        pr1int("\nOrdered Items:")
        for item in order['items']:
            print(f"  - {item:<15} Rs{menu[item]:>4}")
        print("-" * 40)
        print(f"Total Amount: Rs{order['total']:>4}")
        print("-" * 40)
    except Exception as e:
        print(f"Error displaying order: {e}")

def show_orders():
    """Displays all orders that have been placed."""
    print("\n=== ORDER SUMMARY ===")
    try:
        if not orders:
            print("No orders yet.")
            return
        
        sorted_orders = sorted(orders, key=lambda x: x['order_id'])
        for order in sorted_orders:
            print_order(order)
    except Exception as e:
        print(f"Error showing orders: {e}")

def add_menu_item():
    """Add a new item to the menu."""
    print("\n=== Add New Menu Item ===")
    
    while True:
        item_name = input("Enter item name (or 'cancel' to go back): ").strip()
        if item_name.lower() == 'cancel':
            return
        if item_name in menu:
            print("Error: Item already exists in menu!")
            continue
        if not item_name:
            print("Error: Item name cannot be empty!")
            continue
        break
    
    while True:
        try:
            price = float(input("Enter item price: Rs"))
            if price <= 0:
                print("Error: Price must be greater than 0!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number!")
    
    menu[item_name] = price
    save_menu()  # Save menu to file after adding new item
    print(f"\nSuccessfully added {item_name} to menu!")

def remove_menu_item():
    """Remove an item from the menu."""
    print("\n=== Remove Menu Item ===")
    show_menu()
    
    while True:
        item = input("\nEnter item name to remove (or 'cancel' to go back): ").strip()
        if item.lower() == 'cancel':
            return
        
        if item in menu:
            del menu[item]
            save_menu()  # Save menu to file after removing item
            print(f"\nSuccessfully removed {item} from menu!")
            return
        else:
            print(f"Error: '{item}' not found in menu!")

def manage_menu():
    """Menu management submenu."""
    while True:
        print("\n=== MENU MANAGEMENT ===")
        print("1. View Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            show_menu()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            remove_menu_item()
        elif choice == "4":
            showOpt()
            break
        else:
            print("Error: Invalid choice! Please enter a number between 1-4.")

def showOpt(): 
    print("\nOPTIONS:")
    print("1. Show Menu")
    print("2. Take Order")
    print("3. Show Orders")
    print("4. Manage Menu")
    print("5. Exit")

def main():
    """Main function to run the ordering system in a loop."""
    print("Welcome to the Restaurant Order System!")
    
    initialize_data()

    showOpt()
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            show_menu()
            showOpt()
        elif choice == "2":
            take_order()
        elif choice == "3":
            show_orders()
        elif choice == "4":
            manage_menu()
        elif choice == "5":
            print("\nThank you for using the Restaurant Order System!")
            print("Data has been saved to files. See you next time!")
            break
        else:
            print("Error: Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
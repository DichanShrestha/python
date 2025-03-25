from datetime import datetime
import random

# Global constants
MENU = {
    "Momo": 220,
     "Keema Noodles": 200,
    "Samosa Chhaat": 120,
    "Coke": 50
}

# Order status constants
STATUS_CODES = {
    1: "Order Received",
    2: "Preparing",
    3: "Out for Delivery",
    4: "Delivered"
}

# Store orders with their status
orders = {}  # Format: {order_id: {'items': cart, 'status': status_code, 'time': timestamp}}

def generate_order_id():
    """Generate a unique order ID."""
    return f"ORD{random.randint(1000, 9999)}"

def view_menu():
    """Display the menu items and prices."""
    print("\nMENU:")
    for item, price in MENU.items():
        print(f"{item}: ${price:.2f}")

def validate_item(item_name):
    """Normalize and validate item name."""
    normalized = item_name.strip().title()
    return normalized if normalized in MENU else None

def validate_quantity(quantity_str):
    """Validate and convert quantity input."""
    try:
        quantity = int(quantity_str)
        if quantity <= 0:
            print("Quantity must be positive.")
            return None
        return quantity
    except ValueError:
        print("Please enter a valid number.")
        return None

def add_to_cart(cart, item, quantity):
    """Add an item to the cart."""
    normalized_item = validate_item(item)
    if not normalized_item:
        print(f"Sorry, '{item}' is not available in our menu.")
        return cart

    new_cart = cart.copy()
    new_cart[normalized_item] = new_cart.get(normalized_item, 0) + quantity
    print(f"{quantity} {normalized_item}(s) added to cart.")
    return new_cart

def view_cart(cart):
    """Display cart contents and total."""
    print("\nYOUR CART:")
    if not cart:
        print("Cart is empty.")
        return 0

    total = 0
    for item, quantity in cart.items():
        price = MENU[item] * quantity
        print(f"{item} x{quantity} = ${price:.2f}")
        total += price
    print(f"Total: ${total:.2f}")
    return total

def view_order_status(order_id):
    """View the status of a specific order."""
    if order_id not in orders:
        print(f"Order ID {order_id} not found.")
        return

    order = orders[order_id]
    print(f"\nOrder Status for {order_id}")
    print("-" * 30)
    print(f"Status: {STATUS_CODES[order['status']]}")
    print(f"Order Time: {order['time'].strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nOrdered Items:")
    for item, quantity in order['items'].items():
        price = MENU[item] * quantity
        print(f"{item} x{quantity} = ${price:.2f}")
    print(f"Total Amount: ${order['total']:.2f}")

def view_all_orders():
    """View all orders and their statuses."""
    if not orders:
        print("No orders found.")
        return

    print("\nAll Orders:")
    print("-" * 50)
    for order_id, order_info in orders.items():
        print(f"Order ID: {order_id}")
        print(f"Status: {STATUS_CODES[order_info['status']]}")
        print(f"Time: {order_info['time'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total: ${order_info['total']:.2f}")
        print("-" * 50)

def checkout(cart):
    """Process checkout and create new order."""
    if not cart:
        print("Cart is empty. Add items before checkout.")
        return cart, None

    total = view_cart(cart)
    while True:
        confirm = input("Proceed to payment? (yes/no): ").strip().lower()
        if confirm in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'.")

    if confirm == "yes":
        print(f"Processing payment for ${total:.2f}...")
        print("Payment successful! Order confirmed.")
        
        # Create new order
        order_id = generate_order_id()
        orders[order_id] = {
            'items': cart.copy(),
            'status': 1,  # Initial status: Order Received
            'time': datetime.now(),
            'total': total
        }
        
        print(f"\nYour order ID is: {order_id}")
        print("You can use this ID to check your order status.")
        return {}, order_id  # Return empty cart and order ID
    else:
        print("Checkout canceled.")
        return cart, None

def customer_main():
    cart = {}  # Initialize empty cart
    while True:
        try:
            print("\n=== Food Ordering System ===")
            print("1. View Menu\n2. Add to Cart\n3. View Cart")
            print("4. Checkout\n5. Check Order Status")
            print("6. View All Orders\n7. Exit")
            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                view_menu()
            elif choice == "2":
                view_menu()
                item = input("Enter item name: ").strip()
                quantity_str = input("Enter quantity: ").strip()
                quantity = validate_quantity(quantity_str)
                if quantity:
                    cart = add_to_cart(cart, item, quantity)
            elif choice == "3":
                view_cart(cart)
            elif choice == "4":
                cart, order_id = checkout(cart)
            elif choice == "5":
                order_id = input("Enter your order ID: ").strip().upper()
                view_order_status(order_id)
            elif choice == "6":
                view_all_orders()
            elif choice == "7":
                print("Thank you for using our service! Goodbye.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Please try again.")


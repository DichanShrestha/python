import datetime
import os

def send_feedback():
    """Collect and save customer feedback to a file"""
    print("\n=== Feedback Form ===")
    
    # Collect feedback details
    name = input("Your name: ").strip()
    rating = input("Rate your experience (1-5): ").strip()
    comment = input("Your feedback: ").strip()
    
    # Validate rating
    try:
        rating = int(rating)
        if not 1 <= rating <= 5:
            print("Please enter a rating between 1 and 5")
            return False
    except ValueError:
        print("Invalid rating. Please enter a number between 1 and 5")
        return False
    
    # Create feedback entry
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    feedback_entry = (
        f"Time: {timestamp}\n"
        f"Name: {name}\n"
        f"Rating: {rating}/5\n"
        f"Comment: {comment}\n"
        f"{'-' * 50}\n"
    )
    
    # Save feedback to file
    try:
        # Create feedback directory if it doesn't exist
        if not os.path.exists('feedback'):
            os.makedirs('feedback')
        
        # Save to feedback file
        with open('feedback/customer_feedback.txt', 'a', encoding='utf-8') as f:
            f.write(feedback_entry)
        print("\nThank you! Your feedback has been recorded.")
        return True
        
    except Exception as e:
        print(f"\nSorry, couldn't save your feedback: {str(e)}")
        return False

menu = {
    "Momo": 220,
    "Keema Noodles": 200,
    "Samosa Chhat": 120,
    "Coke": 20
}
cart = {}

def view_menu():
    print("\nMENU:")
    for item, price in menu.items():
        print(f"{item}: Rs{price:.2f}")

def add_to_cart(item, quantity):
    if item in menu:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"{quantity} {item}(s) added to cart.")
    else:
        print("Item not available.")

def edit_cart(item, quantity):
    if item in cart:
        if quantity > 0:
            cart[item] = quantity
            print(f"Updated {item} quantity to {quantity}.")
        else:
            delete_from_cart(item)
    else:
        print("Item not in cart.")

def delete_from_cart(item):
    if item in cart:
        del cart[item]
        print(f"Removed {item} from cart.")
    else:
        print("Item not in cart.")

def view_cart():
    print("\nYOUR CART:")
    if not cart:
        print("Cart is empty.")
    else:
        total = 0
        for item, quantity in cart.items():
            price = menu[item] * quantity
            print(f"{item} x{quantity} = ₹{price:.2f}")
            total += price
        print(f"Total: ₹{total:.2f}")

def checkout():
    if not cart:
        print("Cart is empty. Add items before checkout.")
        return
    
    view_cart()
    confirm = input("Proceed to payment? (yes/no): ").strip().lower()
    if confirm == "yes":
        print("Payment successful! Order confirmed.")
        cart.clear()
    else:
        print("Checkout canceled.")

def main():
    while True:
        print("\n1. View Menu\n2. Add to Cart\n3. Edit Cart\n4. Delete from Cart\n5. View Cart\n6. Checkout\n7. Send Feedback\n8. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_menu()
        elif choice == "2":
            item = input("Enter item name: ").strip()
            quantity = int(input("Enter quantity: "))
            add_to_cart(item, quantity)
        elif choice == "3":
            item = input("Enter item name: ").strip()
            quantity = int(input("Enter new quantity: "))
            edit_cart(item, quantity)
        elif choice == "4":
            item = input("Enter item name: ").strip()
            delete_from_cart(item)
        elif choice == "5":
            view_cart()
        elif choice == "6":
            checkout()
        elif choice == "7":
            send_feedback()
        elif choice == "8":
            print("Thank you for visiting! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

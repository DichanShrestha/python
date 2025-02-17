

import os
from datetime import datetime
from update_orders import update_order_status

request = 'D:/py_proj/src/data/ingredient_request.txt'
order_file = 'D:/py_proj/src/data/orders.txt'
ingredient = {}

def show_request():
    if os.path.exists(request):
        with open(request, 'r') as file:
            lines = file.readlines()
            cleaned_lines = [line.strip() for line in lines if line.strip()]
            for line in cleaned_lines:
                print(line)
            return cleaned_lines
    else:
        print("No requests found.")
        return []

def show_orders():
    if os.path.exists(order_file):
        with open(order_file, 'r') as file:
            lines = file.readlines()
            cleaned_lines = [line.strip() for line in lines if line.strip()]
            if not cleaned_lines:
                print("No orders found.")
                return []
            print("\nCurrent Orders:")
            print('-' * 50)
            for line in cleaned_lines:
                print(line)
            print('-' * 50)
            return cleaned_lines
    else:
        print("No orders found.")
        return []

def add_request():
    while True:
        name_of_ingredient = input("Enter Ingredient Name: ").strip()
        if not name_of_ingredient:
            print("Ingredient name cannot be empty!")
            continue
            
        qty_of_ingredient = input("Enter Quantity Required: ").strip()
        if not qty_of_ingredient:
            print("Quantity cannot be empty!")
            continue
        
        ingredient[name_of_ingredient] = qty_of_ingredient
        
        choice = input("Continue? Type 'no' to exit: ").strip().lower()
        if choice == 'no':
            break
    
    existing_data = show_request()
    existing_dict = {}
    
    for line in existing_data:
        if ':' in line:
            name, qty = map(str.strip, line.split(':', 1))
            existing_dict[name] = qty
    
    existing_dict.update(ingredient)
    
    with open(request, 'w') as f:
        for name, qty in existing_dict.items():
            f.write(f"{name}: {qty}\n")
    
    # Create order entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    order_id = f"ORD_{timestamp.replace(' ', '_')}"
    
    with open(order_file, 'a') as f:
        f.write(f"Order ID: {order_id}\n")
        f.write("Items:\n")
        for name, qty in ingredient.items():
            f.write(f"- {name}: {qty}\n")
        f.write(f"Status: Pending\n")
        f.write(f"Date: {timestamp}\n")
        f.write("-" * 30 + "\n")
    
    print(f"\nOrder created successfully! Order ID: {order_id}")
    return order_id

def delete_ingredient(ingredient_name):
    if not os.path.exists(request):
        print("No request file exists.")
        return
        
    ingredient_data = show_request()
    updated_data = []
    found = False
    
    for line in ingredient_data:
        if ':' in line:
            name, _ = map(str.strip, line.split(':', 1))
            if name.lower() != ingredient_name.lower():
                updated_data.append(line)
            else:
                found = True
    
    if not found:
        print(f"Ingredient '{ingredient_name}' not found.")
    else:
        with open(request, 'w') as file:
            file.write('\n'.join(updated_data))
            if updated_data:
                file.write('\n')
        print(f"Ingredient '{ingredient_name}' deleted successfully.")


def req_ingredient():
    while True:
        print('\n' + '=' * 40)
        print("Ingredient Management System")
        print('=' * 40)
        print("1. Show Requested Ingredients")
        print("2. Add Ingredient")
        print("3. Delete Request")
        print("4. Show All Orders")
        print("5. Update Order Status")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        print('=' * 40)
        
        if choice == '1':
            print("\nCurrent Ingredients:")
            print('-' * 20)
            show_request()
        elif choice == '2':
            add_request()
        elif choice == '3':
            item_name = input("Enter item name you want to delete: ").strip()
            delete_ingredient(item_name)
        elif choice == '4':
            show_orders()
        elif choice == '5':
            order_id = input("Enter Order ID: ").strip()
            update_order_status(order_id)
        elif choice == '6':
            print("Thank you for using the system!")
            break
        else:
            print("Invalid Choice! Please enter a number between 1 and 6.")
        
        if choice != '6':
            cont = input("\nContinue with other operations? Type 'no' to stop: ").strip().lower()
            if cont == 'no':
                print("Thank you for using the system!")
                break

if __name__ == "__main__":
    # Create necessary directories if they don't exist
    os.makedirs(os.path.dirname(request), exist_ok=True)
    req_ingredient()
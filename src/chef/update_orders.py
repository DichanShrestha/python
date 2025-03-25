order_file = 'D:/py_proj/src/data/orders.txt'
import os

def update_order_status(order_id):
    if not os.path.exists(order_file):
        print("No orders file exists.")
        return
    
    with open(order_file, 'r') as file:
        lines = file.readlines()
    
    updated_lines = []
    i = 0
    found = False
    
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("Order ID:") and order_id in line:
            found = True
            updated_lines.append(line + '\n')
            # Copy lines until we find the Status line
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("Status:"):
                updated_lines.append(lines[i])
                i += 1
            
            # Update the status
            print("\nCurrent status:", lines[i].strip().split(": ")[1])
            print("1. Mark as Completed")
            print("2. Mark as In Progress")
            print("3. Mark as Cancelled")
            choice = input("Enter your choice (1-3): ").strip()
            
            new_status = "Pending"
            if choice == "1":
                new_status = "Completed"
            elif choice == "2":
                new_status = "In Progress"
            elif choice == "3":
                new_status = "Cancelled"
            
            updated_lines.append(f"Status: {new_status}\n")
            i += 1  # Skip the old status line
            
            # Copy remaining lines of this order
            while i < len(lines) and not lines[i].strip().startswith("Order ID:"):
                updated_lines.append(lines[i])
                i += 1
        else:
            updated_lines.append(lines[i])
            i += 1
    
    if not found:
        print(f"Order ID '{order_id}' not found.")
        return
    
    with open(order_file, 'w') as file:
        file.writelines(updated_lines)
    
    print(f"Order status updated successfully to: {new_status}")

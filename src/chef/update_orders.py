order_file = 'src/data/orders.txt'

def update_order_status(order_id):
    # Check if file exists
    try:
        file = open(order_file, 'r')
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("No orders file exists.")
        return
        
    updated_lines = []
    i = 0
    found = False
    new_status = ""
    
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
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith("Order ID:"):
                updated_lines.append(lines[i])
                i += 1
        else:
            updated_lines.append(lines[i])
            i += 1
    
    if not found:
        print(f"Order ID '{order_id}' not found.")
        return
    
    # Write updated content back to file
    try:
        file = open(order_file, 'w')
        file.writelines(updated_lines)
        file.close()
        print(f"Order status updated successfully to: {new_status}")
    except:
        print("Error writing to file.")

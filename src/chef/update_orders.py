import os

def update_order_status(order_id):
    order_file = 'src/data/orders.txt'
    
    if not os.path.exists(order_file):
        print("No orders file found.")
        return False
    
    with open(order_file, 'r') as file:
        lines = file.readlines()
    
    updated = False
    new_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Split the comma-separated values
        parts = line.split(',')
        if len(parts) >= 5:  # Ensure we have all required parts
            current_order_id = parts[0]
            status_index = 4  # Pending/Completed is the 5th element
            
            if current_order_id == order_id:
                # Update the status to Completed
                parts[status_index] = "Completed"
                updated_line = ','.join(parts)
                new_lines.append(updated_line + '\n')
                updated = True
            else:
                new_lines.append(line + '\n')
        else:
            new_lines.append(line + '\n')
    
    if updated:
        with open(order_file, 'w') as file:
            file.writelines(new_lines)
        print(f"Order {order_id} status updated to Completed.")
        return True
    else:
        print(f"Order {order_id} not found. Please check the ID and try again.")
        return False
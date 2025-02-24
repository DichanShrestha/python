def get_order_status(order_id):
    orders = {
        101: "Processing",
        102: "Shipped",
        103: "Delivered",
        104: "Cancelled"
    }
    
    return orders.get(order_id, "Order not found")

# Get user input
order_id = int(input("Enter your Order ID: "))
print(f"Order Status: {get_order_status(order_id)}")

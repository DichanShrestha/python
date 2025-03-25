Orders_file = "src/data/orders_file.txt"

def view_orders():
    order = []
    try:
        with open(Orders_file) as file:
            order = file.readlines()
    except FileNotFoundError:
        pass  
    return order

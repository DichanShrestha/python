import os

Orders_file="src/data/orders_file.txt"
def view_orders():
    order=[]
    if os.path.exists(Orders_file):
        with open(Orders_file) as file:
            order=file.readlines
    return order   


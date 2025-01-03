import os
SALES_FILE = 'src/data/sales_data.txt'
def view_sales_report():
    sales_report = []
    if os.path.exists(SALES_FILE):
        with open(SALES_FILE) as file:
            sales_report = file.readlines
    return sales_report
    
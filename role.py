from src.admin.manage_staff import manage_staff
from src.admin.view_feedback import view_feedback
from src.admin.view_sales_report import view_sales_report
from src.manager.order_system import main
from src.customer.customer_main import customer_main
from src.chef.request_ingredients import req_ingredient

def choose_role():
    print("Resutrant management system")
    print("===========================")
    print("Choose an option (1/2/3/4) ")
    print("1. Admin")
    print("2. Manager")
    print("3. Chef") 
    print("4. Customer")
    choice = int(input())

    if choice == 1:
        print("Choose an option (1/2/3/4) ")
        print("0. Exit")
        print("1. Manage Staff")
        print("2. Sales Report")
        print("3. View Feedback")
        print("4. Update profile")
        ch = int(input())
        if ch == 1:
            manage_staff()
        elif ch == 2:
            view_sales_report()
        elif ch == 0:
            choose_role()
        elif ch == 3:
            view_feedback()
        elif ch == 4:
            print()
        else:
            print("Invalid choice.")

    elif choice == 2:
       main() 
       choose_role()
    #    manager main
    elif choice == 3:
       req_ingredient()
    elif choice == 4:
        customer_main() 
    else:
        print("Invalid choice.") 
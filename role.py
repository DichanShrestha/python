from src.admin.manage_staff import manage_staff
from src.admin.view_feedback import view_feedback
from src.admin.view_sales_report import view_sales_report

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
        print("1. Manage Staff")
        print("2. Sales Report")
        print("3. View Feedback")
        print("4. Update profile")
        ch = int(input())
        if ch == 1:
            manage_staff()
        elif ch == 2:
            view_sales_report()
        elif ch == 3:
            view_feedback()
        elif ch == 4:
            print()
        else:
            print("Invalid choice.")

    elif choice == 2:
        # manager()
        print()
    elif choice == 3:
        print("Choose an option (1/2/3/4)")
        print("1. View Orders")
        print("2. Update Orders")
        print("3. Request Ingredient")
        print("4. Update Profile")
        ch=int(input())
        if ch==1:
            print('baki xa')
        elif ch==2:
            print("baki xa")
        elif ch==3:
            # req_ingredient()
            print
        elif ch==4:
            print("baki xa")
        else:
            print("Invalid choice")

    else:
        print("Invalid choice.") 
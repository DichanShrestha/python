# File to store staff data
STAFF_DATA_FILE = 'src/data/admin_data.txt'

# A function to read all the staff data from the file
def read_staff_data():
    staff_data = []
    try:
        with open(STAFF_DATA_FILE, 'r') as file:
            staff_data = file.readlines()
    except FileNotFoundError:
        # If file doesn't exist, return empty list
        pass
    return staff_data

# A function to write staff data back to the file
def write_staff_data(staff_data):
    with open(STAFF_DATA_FILE, 'w') as file:
        file.writelines(staff_data)

# Function to add a new staff member
def add_staff(username, role):
    staff_data = read_staff_data()
    new_staff = f"{username},{role}\n"
    staff_data.append(new_staff)
    write_staff_data(staff_data)
    print(f"Staff {username} added successfully.")

# Function to edit an existing staff member
def edit_staff(old_username, new_username, new_role):
    staff_data = read_staff_data()
    for idx, staff in enumerate(staff_data):
        if staff.startswith(old_username):
            staff_data[idx] = f"{new_username},{new_role}\n"
            write_staff_data(staff_data)
            print(f"Staff {old_username} updated to {new_username}.")
            return
    print(f"Staff {old_username} not found.")

# Function to delete a staff member
def delete_staff(username):
    staff_data = read_staff_data()
    for idx, staff in enumerate(staff_data):
        if staff.startswith(username):
            staff_data.pop(idx)
            write_staff_data(staff_data)
            print(f"Staff {username} deleted successfully.")
            return
    print(f"Staff {username} not found.")

# Example of admin managing staff
def manage_staff():
    print("Admin Staff Management")
    print("0. Go Back")
    print("1. Add Staff")
    print("2. Edit Staff")
    print("3. Delete Staff")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        username = input("Enter new staff username: ")
        role = input("Enter staff role (Manager/Chef): ")
        add_staff(username, role)
    elif choice == '2':
        old_username = input("Enter staff username to edit: ")
        new_username = input("Enter new username: ")
        new_role = input("Enter new role: ")
        edit_staff(old_username, new_username, new_role)
    elif choice == '3':
        username = input("Enter staff username to delete: ")
        delete_staff(username)
    elif choice == '0':
        print()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    manage_staff()
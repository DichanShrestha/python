
# Standard Python modules
import os
from role import choose_role

# Global variables to store user data
users = []
users_file = 'src/data/users.txt'
current_user = None

def custom_hash_password(password):
    """
    Custom password hashing without external libraries.
    
    Args:
        password (str): Plain text password
    
    Returns:
        str: Hashed password representation
    """
    # Simple custom hashing method
    salt = 'UserAuth2024'
    hash_value = 0
    for i, char in enumerate(password + salt):
        # Combine character ASCII value with position and salt
        hash_value += (ord(char) * (i + 1)) % 65536
    
    # Convert to hexadecimal and pad
    return f"{hash_value:08x}"

def validate_email(email):
    """
    Basic email validation without regex.
    
    Args:
        email (str): Email to validate
    
    Returns:
        bool: Whether email is valid
    """
    # Check basic email structure
    if not email or '@' not in email or '.' not in email:
        return False
    
    # Split email into parts
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    username, domain = parts
    
    # Check username and domain
    if len(username) < 1 or len(domain) < 3:
        return False
    
    # Check for dot in domain
    if '.' not in domain:
        return False
    
    return True

def validate_password(password):
    """
    Password validation with comprehensive checks.
    
    Args:
        password (str): Password to validate
    
    Returns:
        bool: Whether password meets requirements
    """
    # Check password complexity
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True
    
    return has_upper and has_lower and has_digit and has_special

def generate_user_id():
    """
    Generate a unique user ID.
    
    Returns:
        str: Unique user ID
    """
    # Use a simple method to generate unique ID
    while True:
        # Combine timestamp and user count for uniqueness
        user_id = str(len(users) + 1).zfill(6)
        
        # Ensure ID is unique
        if not any(user['user_id'] == user_id for user in users):
            return user_id

def load_users():
    """
    Load users from text file. 
    Create the file if it doesn't exist.
    
    Returns:
        list: List of user dictionaries
    """
    global users
    users = []
    
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(users_file) or '.', exist_ok=True)
        
        # Try to open and read the file
        with open(users_file, 'r') as f:
            for line in f:
                # Split the line into user attributes
                parts = line.strip().split('|')
                if len(parts) == 4:
                    user = {
                        'user_id': parts[0],
                        'email': parts[1],
                        'password': parts[2],
                        'role': parts[3]
                    }
                    users.append(user)
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open(users_file, 'w'):
            pass
    except IOError:
        print(f"Error reading {users_file}. Using empty user list.")
    
    return users

def save_users():
    """
    Save users to text file using a delimited format.
    """
    try:
        with open(users_file, 'w') as f:
            for user in users:
                # Write user data as a delimited string
                line = f"{user['user_id']}|{user['email']}|{user['password']}|{user['role']}\n"
                f.write(line)
    except IOError:
        print(f"Error saving users to {users_file}")

def register():
    """
    User registration process.
    
    Returns:
        dict: Registered user details or None
    """
    global users
    print("\n--- User Registration ---")
    
    # Email validation
    while True:
        email = input("Enter email address: ").strip()
        if not validate_email(email):
            print("Invalid email format. Please try again.")
            continue
        
        # Check for existing email
        if any(user['email'] == email for user in users):
            print("Email already registered. Please use a different email.")
            continue
        
        break
    
    # Password validation
    while True:
        password = input("Create a password: ")
        confirm_password = input("Confirm password: ")
        
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
        
        if not validate_password(password):
            print("Password must be at least 8 characters and include uppercase, lowercase, digit, and special character.")
            continue
        
        break
    
    # Role selection
    roles = ['Admin', 'Manager', 'Chef', 'Customer']
    print("\nSelect Role:")
    for i, role in enumerate(roles, 1):
        print(f"{i}. {role}")
    
    while True:
        try:
            role_choice = int(input("Enter role number (1-4): "))
            if 1 <= role_choice <= len(roles):
                role = roles[role_choice - 1]
                break
            else:
                print("Invalid role number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Create user profile
    user = {
        'user_id': generate_user_id(),
        'email': email,
        'password': custom_hash_password(password),
        'role': role
    }
    
    users.append(user)
    save_users()  # Save to file immediately after registration
    
    print("\nRegistration Successful!")
    print(f"User ID: {user['user_id']}")
    print(f"Role: {user['role']}")
    
    return user

def login():
    """
    User login process.
    
    Returns:
        dict: Logged-in user details or None
    """
    global current_user
    print("\n--- User Login ---")
    
    # Login attempts
    max_attempts = 3
    for attempt in range(max_attempts):
        email = input("Enter email: ").strip()
        password = input("Enter password: ")
        
        # Hash the input password
        hashed_password = custom_hash_password(password)
        
        # Find user by email and hashed password
        user = next((u for u in users if u['email'] == email and u['password'] == hashed_password), None)
        
        if user:
            current_user = user
            print(f"\nWelcome, {user['role']}!")
            return user
        
        remaining = max_attempts - attempt - 1
        print(f"Invalid credentials. {remaining} attempts remaining.")
    
    print("Too many failed login attempts. Please try again later.")
    return None

def logout():
    """
    Logout current user.
    """
    global current_user
    if current_user:
        print(f"Goodbye, {current_user['role']}!")
        current_user = None
    else:
        print("No user is currently logged in.")

def view_users():
    """
    View all registered users (admin function).
    """
    global current_user
    
    if not current_user or current_user['role'] != 'Admin':
        print("Access denied. Administrator privileges required.")
        return
    
    print("\n--- Registered Users ---")
    for user in users:
        print(f"User ID: {user['user_id']}, Email: {user['email']}, Role: {user['role']}")

def main():
    """
    Main application loop.
    """
    # Load existing users when the program starts
    load_users()
    
    while True:
        print("\n--- User Authentication System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            register()
        elif choice == '2':
            logged_in_user = login()
            if logged_in_user:
                # Logged-in user menu
                choose_role()
        elif choice == '3':
            print("Thank you for using the User Authentication System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()
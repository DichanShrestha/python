# User Authentication System

class UserAuthSystem:
    def __init__(self):
        # Store users as a list of dictionaries
        self.users = []
        # Store current logged-in user
        self.current_user = None

    def validate_email(self, email):
        """Simple email validation."""
        if '@' not in email or '.' not in email:
            return False
        
        # Basic email structure check
        parts = email.split('@')
        if len(parts) != 2 or len(parts[0]) < 1 or len(parts[1]) < 3:
            return False
        
        return True

    def validate_password(self, password):
        """
        Password validation:
        - At least 8 characters
        - Contains uppercase
        - Contains lowercase
        - Contains digit
        """
        if len(password) < 8:
            return False
        
        has_upper = False
        has_lower = False
        has_digit = False
        
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
        
        return has_upper and has_lower and has_digit

    def generate_user_id(self):
        """Generate a unique user ID."""
        import random
        
        # Generate a 6-digit random number
        while True:
            user_id = ''.join(str(random.randint(0, 9)) for _ in range(6))
            
            # Check if ID is unique
            if not any(user['user_id'] == user_id for user in self.users):
                return user_id

    def register(self):
        """User registration process."""
        print("\n--- User Registration ---")
        
        # Email validation
        while True:
            email = input("Enter email address: ").strip()
            if not self.validate_email(email):
                print("Invalid email format. Please try again.")
                continue
            
            # Check for existing email
            if any(user['email'] == email for user in self.users):
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
            
            if not self.validate_password(password):
                print("Password must be at least 8 characters and include uppercase, lowercase, and a digit.")
                continue
            
            break
        
        # Choose role
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
            'user_id': self.generate_user_id(),
            'email': email,
            'password': self.simple_hash(password),  # Basic password hashing
            'role': role
        }
        
        self.users.append(user)
        
        print("\nRegistration Successful!")
        print(f"User ID: {user['user_id']}")
        print(f"Role: {user['role']}")
        
        return user

    def simple_hash(self, password):
        """
        A very basic (NOT cryptographically secure) password hashing.
        In a real system, use proper hashing like bcrypt.
        """
        # Simple hash by summing ASCII values and adding a salt
        salt = 42
        return sum(ord(char) for char in password) + salt

    def login(self):
        """User login process."""
        print("\n--- User Login ---")
        
        # Login attempts
        max_attempts = 3
        for attempt in range(max_attempts):
            email = input("Enter email: ").strip()
            password = input("Enter password: ")
            
            # Find user by email
            user = next((u for u in self.users if u['email'] == email), None)
            
            if user and user['password'] == self.simple_hash(password):
                self.current_user = user
                print(f"\nWelcome, {user['role']}!")
                return user
            
            remaining = max_attempts - attempt - 1
            print(f"Invalid credentials. {remaining} attempts remaining.")
        
        print("Too many failed login attempts. Please try again later.")
        return None

    def logout(self):
        """Logout current user."""
        if self.current_user:
            print(f"Goodbye, {self.current_user['role']}!")
            self.current_user = None
        else:
            print("No user is currently logged in.")

    def view_users(self):
        """View all registered users (admin function)."""
        if not self.current_user or self.current_user['role'] != 'Administrator':
            print("Access denied. Administrator privileges required.")
            return
        
        print("\n--- Registered Users ---")
        for user in self.users:
            print(f"User ID: {user['user_id']}, Email: {user['email']}, Role: {user['role']}")

def main():
    """Main application loop."""
    auth_system = UserAuthSystem()
    
    while True:
        print("\n--- User Authentication System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            auth_system.register()
        elif choice == '2':
            logged_in_user = auth_system.login()
            if logged_in_user:
                # Logged-in user menu
                while True:
                    print("\n--- User Menu ---")
                    print("1. View Users (Admin Only)")
                    print("2. Logout")
                    
                    user_choice = input("Enter your choice (1-2): ").strip()
                    
                    if user_choice == '1':
                        auth_system.view_users()
                    elif user_choice == '2':
                        auth_system.logout()
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Thank you for using the User Authentication System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()
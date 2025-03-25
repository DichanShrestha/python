class ProfileManager:
    def __init__(self, user):
        """
        Initialize ProfileManager with a user dictionary
        User dictionary should have these minimal keys:
        - email
        - password
        - first_name
        - last_name
        - phone
        - address
        - age
        """
        self.user = user

    def validate_email(self, email):
        """Simple email validation."""
        if '@' not in email or '.' not in email:
            return False
        
        parts = email.split('@')
        return len(parts) == 2 and len(parts[0]) >= 1 and len(parts[1]) >= 3

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
        
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        
        return has_upper and has_lower and has_digit

    def update_email(self, new_email, users_list=None):
        """
        Update email with validation
        :param new_email: New email address
        :param users_list: List of all users to check for email uniqueness
        :return: True if successful, False otherwise
        """
        # Validate email format
        if not self.validate_email(new_email):
            print("Invalid email format.")
            return False
        
        # Check email uniqueness if users list is provided
        if users_list:
            if any(user['email'] == new_email for user in users_list if user != self.user):
                print("Email already in use by another account.")
                return False
        
        # Update email
        self.user['email'] = new_email
        print("Email updated successfully.")
        return True

    def update_password(self, current_password, new_password, confirm_password, hash_func=None):
        """
        Update user password
        :param current_password: Current password for verification
        :param new_password: New password
        :param confirm_password: Confirmation of new password
        :param hash_func: Optional hashing function
        :return: True if successful, False otherwise
        """
        # Verify current password
        if hash_func:
            if hash_func(current_password) != self.user['password']:
                print("Incorrect current password.")
                return False
        
        # Check password match
        if new_password != confirm_password:
            print("New passwords do not match.")
            return False
        
        # Validate new password
        if not self.validate_password(new_password):
            print("Password must be at least 8 characters and include uppercase, lowercase, and a digit.")
            return False
        
        # Update password (with optional hashing)
        if hash_func:
            self.user['password'] = hash_func(new_password)
        else:
            self.user['password'] = new_password
        
        print("Password updated successfully.")
        return True

    def update_phone(self, new_phone):
        """
        Update phone number
        :param new_phone: New phone number
        :return: True if successful
        """
        # Optional: Add phone number validation if needed
        self.user['phone'] = new_phone
        print("Phone number updated successfully.")
        return True

    def update_address(self, new_address):
        """
        Update user address
        :param new_address: New address
        :return: True if successful
        """
        self.user['address'] = new_address
        print("Address updated successfully.")
        return True

    def update_age(self, new_age):
        """
        Update user age with validation
        :param new_age: New age
        :return: True if successful, False otherwise
        """
        try:
            age = int(new_age)
            if 0 < age < 120:
                self.user['age'] = age
                print("Age updated successfully.")
                return True
            else:
                print("Please enter a valid age.")
                return False
        except ValueError:
            print("Please enter a valid number.")
            return False

    def update_name(self, first_name=None, last_name=None):
        """
        Update user's first and/or last name
        :param first_name: New first name (optional)
        :param last_name: New last name (optional)
        :return: True if successful
        """
        if first_name is not None:
            self.user['first_name'] = first_name.strip()
        
        if last_name is not None:
            self.user['last_name'] = last_name.strip()
        
        print("Name updated successfully.")
        return True

    def display_profile(self):
        """
        Display current user profile
        """
        print("\n--- User Profile ---")
        for key, value in self.user.items():
            # Avoid displaying sensitive information like password
            if key != 'password':
                print(f"{key.replace('_', ' ').title()}: {value or 'Not provided'}")

def main():
    """
    Example usage of ProfileManager
    """
    # Sample user dictionary
    user = {
        'email': 'john.doe@example.com',
        'password': 'HashedPassword123',
        'first_name': 'John',
        'last_name': 'Doe',
        'phone': '1234567890',
        'address': '123 Main St',
        'age': 30
    }

    # Create ProfileManager instance
    profile_manager = ProfileManager(user)

    # Demonstration of profile update methods
    while True:
        print("\n--- Profile Update Menu ---")
        print("1. Display Profile")
        print("2. Update Email")
        print("3. Update Password")
        print("4. Update Phone")
        print("5. Update Address")
        print("6. Update Age")
        print("7. Update Name")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        try:
            if choice == '1':
                profile_manager.display_profile()
            elif choice == '2':
                new_email = input("Enter new email: ")
                profile_manager.update_email(new_email)
            elif choice == '3':
                current_password = input("Enter current password: ")
                new_password = input("Enter new password: ")
                confirm_password = input("Confirm new password: ")
                profile_manager.update_password(current_password, new_password, confirm_password)
            elif choice == '4':
                new_phone = input("Enter new phone number: ")
                profile_manager.update_phone(new_phone)
            elif choice == '5':
                new_address = input("Enter new address: ")
                profile_manager.update_address(new_address)
            elif choice == '6':
                new_age = input("Enter new age: ")
                profile_manager.update_age(new_age)
            elif choice == '7':
                first_name = input("Enter new first name (leave blank to keep current): ")
                last_name = input("Enter new last name (leave blank to keep current): ")
                profile_manager.update_name(
                    first_name if first_name else None, 
                    last_name if last_name else None
                )
            elif choice == '8':
                print("Exiting profile update.")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
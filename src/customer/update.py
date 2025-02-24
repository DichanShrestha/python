import os

def update_profile(user_id, new_name, new_email):
    # Check if file exists; if not, create it
    if not os.path.exists("profiles.txt"):
        with open("profiles.txt", "w") as file:
            file.write("")  # Create an empty file

    updated_profiles = []
    found = False

    with open("profiles.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")  
            if parts[0] == user_id:  
                updated_profiles.append(f"{user_id},{new_name},{new_email}\n")  
                found = True
            else:
                updated_profiles.append(line)  

    if not found:
        print("User not found! Adding new profile...")
        updated_profiles.append(f"{user_id},{new_name},{new_email}\n")  

    with open("profiles.txt", "w") as file:
        file.writelines(updated_profiles)  

    print("Profile updated successfully!")
    
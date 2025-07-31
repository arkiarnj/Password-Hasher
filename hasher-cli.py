import hashlib
import bcrypt
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hash_md5(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def hash_sha256(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def hash_bcrypt(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def hash_password_menu() -> bool:
    clear_screen()
    print("================================")
    print("        Choose algorithm        ")
    print("================================")
    print("\n")
    print("1. MD5")
    print("2. SHA-256")
    print("3. bcrypt")
    print("4. Return To Main Menu")
    choice = input("Enter choice (1-4): ").strip()

    if choice == "4":
        return False  # برگشت بدون انتظار Enter

    if choice not in ("1", "2", "3"):
        print("❌ Invalid Operation.")
        return True  # منتظر اینتر باش
    print("\n")
    password = input("🔐 Enter your password: ").strip()

    if not password:
        print("Warning, Please enter a password.")
        time.sleep(2)
        return hash_password_menu()
    
    
    print("\nHashed Password:")    
    if choice == "1":
        print(hash_md5(password))
    elif choice == "2":
        print(hash_sha256(password))
    elif choice == "3":
        print(hash_bcrypt(password))

    return True

def about():
    clear_screen()
    print("================================")
    print("             About              ")
    print("================================")
    print("\n")
    print("Password Hasher CLI Tool")
    print("Created by: Arkia RNJ")
    print("Supported algorithms: MD5, SHA-256, bcrypt")
    print("Version: 1.0 (CLI)")

def main_menu():
    while True:
        clear_screen()
        print("=================================")
        print("      Password Hasher Menu       ")
        print("=================================")
        print("\n")
        print("1. Hash a Password")
        print("2. About")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            clear_screen()
            wait_input = hash_password_menu()
        elif choice == "2":
            about()
            wait_input = True
        elif choice == "3":
            break
        else:
            print("❌ Invalid option. Try again.")
            wait_input = True

        if wait_input:
            input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    clear_screen()
    main_menu()
    
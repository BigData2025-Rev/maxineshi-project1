from features.users import create_user, login_user, check_username_exists
from features.products import get_all_products
from features.orders import create_order, get_user_orders
from admin import admin_panel
import getpass
from utils import logger  # Assuming logger is defined in utils.py

def main():
    logger.info("Application started: Pokémon Card Store")
    print("Welcome to the Pokémon Card Store!")
    
    while True:
        print("\n[1] Register")
        print("[2] Login")
        print("[3] Exit")
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            logger.warning("Invalid input: Non-numeric value entered for main menu choice.")
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            # User Registration
            while True:
                username = input("Enter a username: ")
                if check_username_exists(username):
                    logger.warning(f"Registration failed: Username '{username}' already exists.")
                    print("Error: Username already exists. Please choose a different username.")
                else:
                    break

            password = getpass.getpass("Enter a password: ")
            result = create_user(username, password)
            logger.info(f"User registered successfully: {username}")
            print(result)
        
        elif choice == 2:
            # User Login
            username = input("Enter your username: ")
            if not check_username_exists(username):
                logger.warning(f"Login failed: Username '{username}' does not exist.")
                print("Error: Username does not exist.")
                continue

            password = getpass.getpass("Enter your password: ")
            login_result = login_user(username, password)
            
            if login_result["success"]:
                logger.info(f"User logged in successfully: {username}")
                print(login_result["message"])
                user = login_result["user"]
                
                if user["role"] == "admin":
                    logger.info("Admin accessed the admin panel.")
                    admin_panel()
                else:
                    # User Actions
                    while True:
                        print("\n[1] Browse Products")
                        print("[2] View Orders")
                        print("[3] Logout")
                        try:
                            action = int(input("Choose an option: "))
                        except ValueError:
                            logger.warning("Invalid input: Non-numeric value entered for user actions.")
                            print("Invalid input. Please enter a number.")
                            continue
                        
                        if action == 1:
                            products = get_all_products()
                            logger.info(f"User '{username}' browsed products.")
                            for product in products:
                                print(product)
                        elif action == 2:
                            orders = get_user_orders(user["_id"])
                            logger.info(f"User '{username}' viewed their orders.")
                            for order in orders:
                                print(order)
                        elif action == 3:
                            logger.info(f"User '{username}' logged out.")
                            print("Logging out...")
                            break
                        else:
                            logger.warning("Invalid option selected in user actions.")
                            print("Invalid option. Try again.")
            else:
                logger.warning(f"Login failed for username '{username}': {login_result['message']}")
                print(login_result["message"])
        
        elif choice == 3:
            logger.info("Application exited.")
            print("Goodbye!")
            break
        
        else:
            logger.warning("Invalid option selected in the main menu.")
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

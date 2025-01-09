from features.users import create_user, login_user, check_username_exists
from features.products import get_all_products
from features.orders import create_order, get_user_orders
from admin import admin_panel
from utils import logger
import getpass

def main():
    print("Welcome to the Pokémon Card Store!")
    while True:
        print("[1] Register")
        print("[2] Login")
        print("[3] Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            # Registration Process
            username = input("Enter a username: ")
            if check_username_exists(username):
                logger.warning("Error: Username already exists. Please choose a different username.")
                continue

            password = getpass.getpass("Enter a password: ")
            result = create_user(username, password)
            print(result)

        elif choice == 2:
            # Login Logic
            username = input("Username: ")
            if not check_username_exists(username):
                logger.warning("Error: Username does not exists. Please ensure the username is correct.")
                continue
            password = getpass.getpass("Password: ")
            login_result = login_user(username, password)
            if login_result["success"]:
                print(login_result["message"])
                user = login_result["user"]
                if user["role"] == "admin":
                    admin_panel()
                else:
                    while True:
                        print("\n[1] Browse Products")
                        print("[2] View Orders")
                        print("[3] Logout")
                        action = int(input("Choose an option: "))
                        if action == 1:
                            products = get_all_products()
                            for product in products:
                                print(product)
                        elif action == 2:
                            orders = get_user_orders(user["_id"])
                            for order in orders:
                                print(order)
                        elif action == 3:
                            print("Logging out...")
                            break
                        else:
                            print("Invalid option. Try again.")
            else:
                print(login_result["message"])

        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")



if __name__ == "__main__":
    main()

from features.users import create_user, login_user, check_username_exists
from features.products import get_all_products
from features.orders import create_order, get_user_orders
from admin import admin_panel
from utils import logger
import getpass

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
            logger.warning("Invalid input: Non-numeric value entered in main menu.")
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            # Registration Process
            username = input("Enter a username: ")
            if check_username_exists(username):
                logger.warning("Error: Username already exists. Please choose a different username.")
                print("Error: Username already exists. Please choose a different username.")
                continue

            password = getpass.getpass("Enter a password: ")
            result = create_user(username, password)
            logger.info(f"User registered successfully: {username}")
            print(result)

        elif choice == 2:
            # Login Logic
            username = input("Username: ")
            if not check_username_exists(username):
                logger.warning("Error: Username does not exist. Please ensure the username is correct.")
                print("Error: Username does not exist.")
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
                        print("[3] Place an Order")
                        print("[4] Logout")
                        try:
                            action = int(input("Choose an option: "))
                        except ValueError:
                            logger.warning("Invalid input: Non-numeric value entered in user actions.")
                            print("Invalid input. Please enter a number.")
                            continue

                        if action == 1:
                            # Browse Products
                            products = get_all_products()
                            print("\n--- Available Products ---")
                            for product in products:
                                print(f"ID: {product['_id']}, Name: {product['name']}, Price: ${product['price']}, Stock: {product['stock']}")

                        elif action == 2:
                            # View Orders
                            orders = get_user_orders(user["_id"])
                            print("\n--- Your Orders ---")
                            for order in orders:
                                print(f"Order ID: {order['_id']}, Total Price: ${order['total_price']}, Date: {order['order_date']}")

                        elif action == 3:
                            # Place an Order
                            print("\n--- Place an Order ---")
                            products = get_all_products()
                            print("\nAvailable Products:")
                            for idx, product in enumerate(products, start=1):
                                print(f"{idx}. Name: {product['name']}, Price: ${product['price']}, Stock: {product['stock']}")

                            selected_products = []
                            while True:
                                product_choice = input("Enter the product number to add to your order (or 'done' to finish): ")
                                if product_choice.lower() == "done":
                                    break
                                try:
                                    product_idx = int(product_choice) - 1
                                    if 0 <= product_idx < len(products):
                                        product = products[product_idx]
                                        quantity = int(input(f"Enter quantity for {product['name']}: "))
                                        if quantity <= product["stock"]:
                                            selected_products.append({
                                                "product_id": product["_id"],
                                                "price": product["price"],
                                                "quantity": quantity
                                            })
                                            print(f"Added {quantity} x {product['name']} to your order.")
                                        else:
                                            print(f"Insufficient stock for {product['name']}. Available stock: {product['stock']}.")
                                    else:
                                        print("Invalid product number. Please try again.")
                                except (ValueError, IndexError):
                                    print("Invalid input. Please enter a valid product number.")

                            if selected_products:
                                result = create_order(user["_id"], selected_products)
                                print(result)
                                logger.info(f"Order placed successfully for user '{username}'.")
                            else:
                                print("No products selected for the order.")

                        elif action == 4:
                            # Logout
                            logger.info(f"User '{username}' logged out.")
                            print("Logging out...")
                            break

                        else:
                            print("Invalid option. Try again.")

            else:
                logger.warning(f"Login failed for username '{username}': {login_result['message']}")
                print(login_result["message"])

        elif choice == 3:
            # Exit
            logger.info("Application exited.")
            print("Goodbye!")
            break

        else:
            logger.warning("Invalid option selected in main menu.")
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

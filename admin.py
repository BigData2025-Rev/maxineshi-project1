from features.users import get_all_users, update_user_role, delete_user
from features.products import add_product, delete_product
from features.orders import get_all_orders
from utils import logger

def admin_panel():
    """Admin panel interface."""
    logger.info("Admin accessed the admin panel.")
    print("Welcome to the Admin Panel!")

    while True:
        print("\n[1] View all users")
        print("[2] Update user role")
        print("[3] Delete a user")
        print("[4] Add a product")
        print("[5] Delete a product")
        print("[6] View all orders")
        print("[7] Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            logger.warning("Invalid input: Non-numeric value entered in admin panel.")
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            # View all users
            users = get_all_users()
            logger.info("Admin viewed all users.")
            print("\n--- Users ---")
            for user in users:
                print(user)
        
        elif choice == 2:
            # Update user role
            username = input("Enter username: ")
            new_role = input("Enter new role: ")
            result = update_user_role(username, new_role)
            logger.info(f"Admin updated role for user '{username}' to '{new_role}'.")
            print(result)
        
        elif choice == 3:
            # Delete a user
            username = input("Enter username to delete: ")
            result = delete_user(username)
            logger.info(f"Admin deleted user '{username}'.")
            print(result)
        
        elif choice == 4:
            # Add a product
            name = input("Product name: ")
            description = input("Description: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
            except ValueError:
                logger.warning("Invalid input: Non-numeric value entered for product price or stock.")
                print("Invalid input. Price must be a number and stock must be an integer.")
                continue
            category = input("Category: ")
            result = add_product(name, description, price, stock, category)
            logger.info(f"Admin added product '{name}'.")
            print(result)
        
        elif choice == 5:
            # Delete a product
            product_id = input("Enter product ID to delete: ")
            result = delete_product(product_id)
            logger.info(f"Admin deleted product with ID '{product_id}'.")
            print(result)
        
        elif choice == 6:
            # View all orders
            orders = get_all_orders()
            logger.info("Admin viewed all orders.")
            print("\n--- Orders ---")
            for order in orders:
                print(order)
        
        elif choice == 7:
            # Exit admin panel
            logger.info("Admin exited the admin panel.")
            print("Goodbye!")
            break
        
        else:
            logger.warning(f"Invalid option selected: {choice}")
            print("Invalid option. Try again.")

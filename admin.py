from features.users import get_all_users, update_user_role, delete_user
from features.products import add_product, delete_product
from features.orders import get_all_orders

def admin_panel():
    """Simple admin interface."""
    print("Welcome, Admin!")
    print("[1] View all users")
    print("[2] Update user role")
    print("[3] Delete a user")
    print("[4] Add a product")
    print("[5] View all orders")
    print("[6] Exit")

    choice = int(input("Choose an option: "))
    if choice == 1:
        users = get_all_users()
        print(users)
    elif choice == 2:
        username = input("Enter username: ")
        new_role = input("Enter new role: ")
        print(update_user_role(username, new_role))
    elif choice == 3:
        username = input("Enter username to delete: ")
        print(delete_user(username))
    elif choice == 4:
        name = input("Product name: ")
        description = input("Description: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        category = input("Category: ")
        print(add_product(name, description, price, stock, category))
    elif choice == 5:
        orders = get_all_orders()
        print(orders)
    elif choice == 6:
        print("Goodbye!")

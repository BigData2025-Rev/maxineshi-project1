from datetime import datetime
from db.connection import get_db
from utils import logger  # Assuming you have a logger setup in utils.py

db = get_db("orders")

def create_order(user_id, products):
    """
    Create a new order.

    Args:
        user_id (str): ID of the user placing the order.
        products (list): A list of dictionaries with 'product_id', 'price', and 'quantity'.

    Returns:
        str: A success message or error message.
    """
    try:
        # Calculate total price
        total_price = sum([product["price"] * product["quantity"] for product in products])

        # Create order structure
        order = {
            "user_id": user_id,
            "products": products,
            "total_price": total_price,
            "order_date": datetime.now(),
        }

        # Insert order into the database
        db.orders.insert_one(order)
        logger.info(f"Order created successfully for user_id '{user_id}' with total price {total_price}.")
        return "Order placed successfully."
    except Exception as e:
        logger.error(f"Failed to create order for user_id '{user_id}': {e}")
        return "Failed to place order. Please try again later."

def get_user_orders(user_id):
    """
    Retrieve a user's order history.

    Args:
        user_id (str): ID of the user.

    Returns:
        list: A list of orders for the specified user.
    """
    try:
        orders = list(db.orders.find({"user_id": user_id}))
        logger.info(f"Retrieved {len(orders)} orders for user_id '{user_id}'.")
        return orders
    except Exception as e:
        logger.error(f"Failed to retrieve orders for user_id '{user_id}': {e}")
        return []

def get_all_orders():
    """
    Retrieve all orders (Admin Only).

    Returns:
        list: A list of all orders.
    """
    try:
        orders = list(db.orders.find({}))
        logger.info(f"Admin retrieved all orders. Total orders: {len(orders)}.")
        return orders
    except Exception as e:
        logger.error(f"Failed to retrieve all orders: {e}")
        return []

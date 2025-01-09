from datetime import datetime
from db.connection import get_db

db = get_db()

def create_order(user_id, products):
    """Create a new order."""
    total_price = sum([product["price"] * product["quantity"] for product in products])
    order = {
        "user_id": user_id,
        "products": products,
        "total_price": total_price,
        "order_date": datetime.now(),
    }
    db.orders.insert_one(order)
    return "Order placed successfully."

def get_user_orders(user_id):
    """Retrieve a user's order history."""
    return list(db.orders.find({"user_id": user_id}))

def get_all_orders():
    """Retrieve all orders (Admin Only)."""
    return list(db.orders.find({}))

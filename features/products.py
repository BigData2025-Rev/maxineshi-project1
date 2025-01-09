from db.connection import get_db

db = get_db()

def add_product(name, description, price, stock, category):
    """Add a new product to the inventory."""
    product = {
        "name": name,
        "description": description,
        "price": price,
        "stock": stock,
        "category": category,
    }
    db.products.insert_one(product)
    return f"Product {name} added to inventory."

def get_all_products():
    """Retrieve all products."""
    return list(db.products.find({}))

def update_product_stock(product_id, new_stock):
    """Update a product's stock."""
    db.products.update_one({"_id": product_id}, {"$set": {"stock": new_stock}})
    return f"Product {product_id} stock updated."

def delete_product(product_id):
    """Delete a product."""
    db.products.delete_one({"_id": product_id})
    return f"Product {product_id} deleted."

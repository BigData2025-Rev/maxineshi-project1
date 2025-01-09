from typing import List, Union
from bson.objectid import ObjectId
from db.connection import get_db

db = get_db()

def add_product(name: str, description: str, price: float, stock: int, category: str) -> str:
    """Add a new product to the inventory."""
    if not isinstance(name, str) or not isinstance(description, str) or not isinstance(price, (int, float)) or not isinstance(stock, int) or not isinstance(category, str):
        raise TypeError("Invalid input types.")
    
    product = {
        "name": name,
        "description": description,
        "price": price,
        "stock": stock,
        "category": category,
    }
    db.products.insert_one(product)
    return f"Product {name} added to inventory."

def get_all_products() -> Union[str, List[dict]]:
    """Retrieve all products."""
    products = list(db.products.find({}))
    if not products:
        return "No current products."
    return products

def update_product_stock(product_id: str, new_stock: int) -> str:
    """Update a product's stock."""
    if not ObjectId.is_valid(product_id) or not isinstance(new_stock, int):
        raise TypeError("Invalid input types.")
    
    db.products.update_one({"_id": ObjectId(product_id)}, {"$set": {"stock": new_stock}})
    return f"Product {product_id} stock updated."

def delete_product(product_id: str) -> str:
    """Delete a product."""
    if not ObjectId.is_valid(product_id):
        raise TypeError("Invalid input types.")
    
    db.products.delete_one({"_id": ObjectId(product_id)})
    return f"Product {product_id} deleted."

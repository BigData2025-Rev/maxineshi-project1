from datetime import datetime
from db.connection import get_db
from utils import hash_password, check_password
from utils import logger

db = get_db()

def check_username_exists(username):
    """Check if the username already exists."""
    return db.users.find_one({"username": username}) is not None

def create_user(username, password):
    """Create a new user."""
    hashed_pw = hash_password(password)
    user = {
        "username": username,
        "password": hashed_pw,
        "role": "user",
        "created_at": datetime.now(),
    }
    db.users.insert_one(user)
    return "User registered successfully."

def login_user(username, password):
    """Log in a user."""
    user = db.users.find_one({"username": username})
    if not user:
        logger.warning(f"Login failed: Username '{username}' not found.")
        return {"success": False, "message": "Username not found."}
    if not check_password(password, user["password"]):
        logger.warning(f"Login failed: Incorrect password for username '{username}'.")
        return {"success": False, "message": "Invalid password."}
    logger.info(f"User '{username}' logged in successfully.")
    return {"success": True, "message": f"Welcome back, {username}!", "user": user}



def get_all_users():
    """Retrieve all users (Admin Only)."""
    return list(db.users.find({}, {"password": 0}))

def update_user_role(username, new_role):
    """Update a user's role (Admin Only)."""
    db.users.update_one({"username": username}, {"$set": {"role": new_role}})
    return f"{username}'s role updated to {new_role}."

def delete_user(username):
    """Delete a user (Admin Only)."""
    db.users.delete_one({"username": username})
    return f"User {username} deleted."

import bcrypt
import logging

logging.basicConfig(level=logging.INFO)

def hash_password(password):
    """Hash the user's password."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def check_password(password, hashed):
    """Verify a password."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

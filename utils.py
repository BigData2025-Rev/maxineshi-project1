import bcrypt
import logging

logging.basicConfig(level=logging.INFO)

def hash_password(password):
    """Hash the user's password."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def check_password(password, hashed):
    """Verify a password."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

logger = logging.getLogger(__name__)

if not logger.hasHandlers():
    logger.setLevel(logging.DEBUG)

    # Create a console handler and set the level to DEBUG
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)
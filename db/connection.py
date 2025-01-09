import os
from dotenv import load_dotenv
from pymongo import MongoClient
from utils import logger

load_dotenv()

def get_db():
    """Connect to MongoDB and return the database."""

    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    try:
        client.admin.command("ping")
        logger.info("Connected to MongoDB successfully.")
        return client["pokemon_store"]
    except Exception as e:
        logger.error("Failed to connect to MongoDB: %s", e)
        raise

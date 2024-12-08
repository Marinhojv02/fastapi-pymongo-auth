
# GENERIC LIB
from pymongo import MongoClient
# COLLECTIONS
# MODEL
# UTILS
from app.utils.config import Config

client = MongoClient()
uri = f"mongodb://{Config.DB.USER}:{Config.DB.PASSWORD}@{Config.DB.HOST}/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client[Config.DB.DATABASE]

user_collection = db["users"]
product_collection = db["products"]
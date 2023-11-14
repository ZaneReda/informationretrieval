from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Replace with your MongoDB URI
uri = "mongodb+srv://<username>:<password>@recosystems.hyjorhd.mongodb.net/?retryWrites=true&w=majority"



def set_user():
    if os.environ.get('MongoDBpassword') and os.environ.get('MongoDBuser'):
        del os.environ["MongoDBpassword"]
        del os.environ["MongoDBuser"]
    load_dotenv()
    password = os.getenv('MongoDBpassword')
    username = os.getenv('MongoDBuser')
    return username, password

username, password = set_user()
uri = uri.replace('<username>', username)
uri = uri.replace('<password>', password)


client = MongoClient(uri)

try:
    # Perform a simple operation like listing database names
    print(client.list_database_names())
    print("MongoDB server is available.")
except Exception as e:
    print("Failed to connect to MongoDB server:", e)

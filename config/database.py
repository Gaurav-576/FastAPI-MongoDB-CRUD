from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
email_id = os.getenv('MONGODB_EMAIL_ID')
password = os.getenv('MONGODB_PASSWORD')

client=MongoClient("mongodb+srv://gauravsingh96753:XLhZeXRCZUVXuXro@fastapi.e1lh6.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI")
db=client.treasure_hunt_2k25
collection_name=db["questions"]
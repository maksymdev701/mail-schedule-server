from utils.loader import parse_json_file
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from core.config import db_name

# load environment variables from .env file
load_dotenv()

# connect to the MongoDB server
client = MongoClient(os.getenv("MONGO_URI"))

# the database working with this project
db = client.get_database(db_name)


def load_threads():
    # load json objects from big json file
    json_interator = parse_json_file(
        "resources/example_emails/json/veronica_emails.json")

    # select collection where data to be inserted
    threads = db["threads"]

    for obj in json_interator:
        del obj["_id"]
        threads.insert_one(obj)


def put_documents(thread: dict):

    return ""


if __name__ == "__main__":
    thread_cuont = db["threads"].count_documents({})
    if thread_cuont == 0:
        load_threads()

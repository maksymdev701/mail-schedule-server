import pymongo
import os
from dotenv import load_dotenv
from loader import parse_json_file

# Load environment variables from the .env file
load_dotenv()

client = pymongo.MongoClient(os.getenv('MONGO_URI'))
db = client["daystream"]


def load_threads():
    json_interator = parse_json_file(
        "./example_emails/json/veronica_emails.json")

    threads = db["threads"]

    for obj in json_interator:
        del obj["_id"]
        threads.insert_one(obj)


# Load email thread json file and insert it into mongo datbase
load_threads()

from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Get the MongoDB password from the environment variables
password = os.environ.get("MONGO_PASSWORD")

# Set up the MongoDB connection string
connection_string = f"mongodb+srv://cmkdesignpro:{password}@todolist.viqo0ng.mongodb.net/?retryWrites=true&w=majority"

# Connect to the MongoDB client
client = MongoClient(connection_string)

# Get the 'Tasks' database
db = client.get_database("Tasks")


def add_task(task, status):
    # Add a task to the database
    id = db.Tasks.insert_one({"task": task, "status": status}).inserted_id
    return id


def get_tasks():
    # Get all tasks from the database
    tasks = db.Tasks.find()
    new_tasks = []
    for task in tasks:
        new_tasks.append(task)
    return new_tasks


def delete_task(id):
    # Delete a task from the database based on its ObjectId
    from bson.objectid import ObjectId
    db.Tasks.delete_one({"_id": ObjectId(id)})


def mark_complete(id, status):
    # Mark a task as complete or incomplete in the database based on its ObjectId
    from bson.objectid import ObjectId
    db.Tasks.update_one({"_id": ObjectId(id)}, {"$set": {"status": status}})

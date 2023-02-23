from pymongo import MongoClient

"""
Method get_db creates a connection to the mongodb server and connects to the database "wwi21amb"
"""


async def get_db():
    # DB URL with credentials → Unsecure...
    db_url_string = "mongodb://backend:wwi21amb_backend@83.229.85.86/wwi21amb"

    # Create a client
    client = MongoClient(db_url_string)

    # Returns DB "wwi21amb"
    return client['wwi21amb']


if __name__ == "__main__":
    # Get DB connection
    dbname = get_db()

    """
    #For testing purposes
    
    collection = dbname["wwi21amb"]

    test = collection.find()

    for test_input in test:
        print(test_input)

    """

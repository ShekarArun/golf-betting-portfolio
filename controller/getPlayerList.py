from dns.resolver import query
import requests
import os
import pymongo
import pandas as pd

db_name = os.getenv("DB_NAME")


def handler(event, context):
    """Main endpoint handler

    Orchestrator function which accepts event and context objects, and returns a response status

    Input:
    event: Event object
    context: Context object

    Returns:
    response: Response and status of execution"""
    global db_name

    url = "https://golf-leaderboard-data.p.rapidapi.com/entry-list/293"

    headers = {
        "x-rapidapi-key": "57dc5fb767msh5a323bce509a21ep17b1c5jsn24618c6b6183",
        "x-rapidapi-host": "golf-leaderboard-data.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers)
    response_data = response.json()
    players = pd.json_normalize(response_data["results"]["entry_list"])

    # Check DB if entry of player list present for that month before calling API
    try:
        Player_List_Collection = get_db_client(db_name, os.getenv("COLL_NAME_LISTS"))
        print()
        # TODO: Build query based on tournament ID and list type
        query = {}
        player_list = Player_List_Collection.find(query)
        # TODO: Store fresh list if not found
    except Exception as e:
        print(
            {
                "error_key": "db_connection_error",
                "error_subkey": "lists_coll_conn_error",
                "message": "Error connecting to database",
                "error": e,
            }
        )
        raise e


def get_db_client(db, collection):
    """Returns a client connected to the specific DB collection"""

    try:
        connection_url = os.getenv("DB_URI")
        client = pymongo.MongoClient(connection_url)

        # Access database
        Database = client.get_database(db)
        # Access collection
        return Database[collection]
    except Exception as e:
        print("Error connecting to database: ", e)


if __name__ == "__main__":
    os.environ[
        "DB_URI"
    ] = "mongodb+srv://nodeDev:nOp14JgNo9oaZjSq@arunmongo1.xxxhu.mongodb.net/golf-portfolio-proto?retryWrites=true&w=majority"
    os.environ["COLL_NAME_LISTS"] = "list"
    os.environ["DB_NAME"] = "golf-portfolio-proto"
    handler("", "")

import requests
import pandas as pd


def handler(event, context):
    """Main endpoint handler

    Orchestrator function which accepts event and context objects, and returns a response status

    Input:
    event: Event object
    context: Context object

    Returns:
    response: Response and status of execution"""
    url = "https://golf-leaderboard-data.p.rapidapi.com/entry-list/293"

    headers = {
        "x-rapidapi-key": "57dc5fb767msh5a323bce509a21ep17b1c5jsn24618c6b6183",
        "x-rapidapi-host": "golf-leaderboard-data.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers)
    response_data = response.json()
    players = pd.json_normalize(response_data["results"]["entry_list"])

    # TODO:
    # Check DB if entry present for that month before calling API
    # If found, return that
    # If not found, fetch, store in DB and return


if __name__ == "__main__":
    handler("", "")

player_list_schema = {
    "id": {"type": "string"},
    # List type indicates if the list is a system generated or user generated list
    # 1 - List of all players in a tournament (System generated)
    # 2 - List created by user
    "type": {"type": "int"},
    "name": {"type": "string"},
    "players": [
        {
            "api_player_id": {"type": "int"},
            "first_name": {"type": "string"},
            "last_name": {"type": "string"},
            "country_code": {"type": "string"},
        }
    ],
    "min_win_score": {"type": "int"},
    "tournament": {
        "api_tournament_id": {"type": "string"},
        "type": {"type": "string"},  # Can have enum "STROKE_PLAY","MATCH_PLAY", etc
        "tour_id": {"type": "int"},
        "name": {"type": "string"},
        "country": {"type": "string"},
        "course": {"type": "string"},
        "start_date": {"type": "date"},
        "end_date": {"type": "date"},
        "timezone": {"type": "timezone"},
        "prize_fund": {"type": "float"},
        "fund_currency": {"type": "string"},  # enum USD, INR, etc
    },
    "user": {
        # Information about the user to whom this list belongs
        "id": {"type": "string"},
        "name": {"type": "string"},
    },
    # Added at date is the midnight timestamp of the date when the list was added
    # (if it needs to be fetched by date for some reason)
    "added_date": {"type": "date"},
    "created_at": {"type": "date"},
    "updated_at": {"type": "date"},
}

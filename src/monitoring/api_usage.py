import json
import os
from datetime import date

LIMIT = 20

FILE_NAME = "api_usage.json"


def _load():

    if not os.path.exists(FILE_NAME):
        return {
            "date": str(date.today()),
            "count": 0,
        }

    with open(FILE_NAME, "r") as f:
        data = json.load(f)

    # Reset automatically if a new day starts
    if data["date"] != str(date.today()):
        data = {
            "date": str(date.today()),
            "count": 0,
        }

    return data


def _save(data):

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def record_api_call():

    data = _load()

    data["count"] += 1

    _save(data)


def get_usage():

    data = _load()

    used = data["count"]

    remaining = max(0, LIMIT - used)

    return used, remaining
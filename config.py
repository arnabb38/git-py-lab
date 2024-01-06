# config.py

import json


def load_credentials():
    with open("credential.json") as f:
        credentials = json.load(f)
        return credentials

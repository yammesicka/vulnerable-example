# Credit
# Param list (`param_names.txt`) is taken from:
# https://raw.githubusercontent.com/whiteknight7/wordlist/main/fuzz-lfi-params-list.txt

import requests

AUTH_DETAILS = {"username": "john", "password": "password123"}
URL = "http://localhost:5000"

with requests.Session() as s:
    requests.get(f"{URL}/login", params=AUTH_DETAILS)
    r = s.get(f"{URL}/leaderboard")
    regular_response = r.text
    with open("param_names.txt", "r") as f:
        for line in f:
            param = line.strip()
            response = s.get(f"{URL}/leaderboard", params={param: "test"})
            if response.text != regular_response:
                print(f"Found param: {param}")

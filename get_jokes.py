import json
import requests


def get_dad_jokes():
    """gets dad jokes from icanhazdadjoke.com"""

    url = "https://icanhazdadjoke.com/search"
    headers = {"User-Agent": "https://github.com/agstaples",
               "Accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

print(get_dad_jokes())
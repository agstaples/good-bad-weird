import json
import requests


def get_dad_jokes():
    """gets dad jokes from icanhazdadjoke.com"""

    page_num = 1
    page_results = []

    while page_num < 23:
        url = f"https://icanhazdadjoke.com/search?page={page_num}"
        headers = {"User-Agent": "https://github.com/agstaples",
               "Accept": "application/json"}
        response = requests.get(url, headers=headers)
        page_num += 1
        if response.status_code == 200:
            response_json = json.loads(response.content.decode('utf-8'))
            page_results.append(response_json["results"])

    return page_results

def save_dad_joke_text():
    """saves joke text from response json"""

    page_results = get_dad_jokes()

    file = open("data/joke-text.txt", "w")
    for results in page_results:
        for result in results:
            file.write(result["joke"]+"\n")

def get_dad_joke_string():
    """returns joke text as single string with each joke ending in new line"""

    joke_string = ""

    file = open("data/joke-text.txt", "r")
    joke_string = file.read()

    return joke_string



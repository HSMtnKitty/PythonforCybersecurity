import requests

def get_dad_jokes():
    url = "https://icanhazdadjoke.com/"

    #header to specify jaon response
    headers = {
        "Accept": "application/json"
    }

    #send out get request to API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        joke_data = response.json()

        print(joke_data['joke'])
    else print(f"Failed to retrieve joke. Status code: {response.status_code}")
    
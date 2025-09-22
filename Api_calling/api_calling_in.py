import requests as rq

# Make get request
response = rq.get("https://official-joke-api.appspot.com/random_joke")

# Check status
if response.status_code == 200:
    data = response.json()
    print("Here is a joke for you: ")
    print(data["setup"])
    print(data["punchline"])
else:
    print("Error: ", response.status_code)

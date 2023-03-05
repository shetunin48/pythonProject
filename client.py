import requests
import json

# TODO: user
headers = requests.utils.default_headers()

headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

json_string = {
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    },
    "spaceship": "spoon"
}
x = json.dumps(json_string)
ans = requests.post("http://127.0.0.5:8000//keys", bytearray(x, "utf-8"), headers=headers)
print(ans)

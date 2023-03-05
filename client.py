import requests
import json

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
    }
}
x = json.dumps(json_string)

print(requests.post("http://127.0.0.5:8000//keys", bytearray(x, "utf-8")))

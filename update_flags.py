import json
import os.path

import requests


r = requests.get("https://raw.githubusercontent.com/mledoze/countries/master/dist/countries-unescaped.json")
data = r.json()

flags = {country["cca3"]: country["flag"] for country in data}

with open("flags.json", "w") as f:
    json.dump(flags, f, ensure_ascii=False, indent=2)

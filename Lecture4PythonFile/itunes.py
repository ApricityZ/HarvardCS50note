import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()  # 退出整个程序,不同于break

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o["results"]:
    print(result["trackName"])
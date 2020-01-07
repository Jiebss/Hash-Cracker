#!/usr/bin/python3.6
import requests, json

print("This script uses the Hashes.org API. Please use it with respect.")
print("Usage is limited to 20 hashes per minute enforced by checking during a 5 minute window.")

check_hash = input("Enter your hash: ")
api = "YOUR API KEY"
parameters = {"key": api, "query": check_hash}

response = requests.get("https://hashes.org/api.php", params=parameters)

st = json.loads(response.content)

status = st["status"]
succes = st["result"][check_hash]

if succes is not None and "plain" in succes:
    plain = st["result"][check_hash]["plain"]
    hexplain = st["result"][check_hash]["hexplain"]
    algorithm = st["result"][check_hash]["algorithm"]

    #start results
    print("-------------------------------------------------------")
    print("Status:   ", status)
    print("Your hash:", check_hash)
    print("Plain:    ", plain)
    print("Hexplain: ", hexplain)
    print("Algorithm:", algorithm)
    print("-------------------------------------------------------")
    #end results
elif succes is None:
    print("-------------------------------------------------------")
    print("Hash was not found.")
    print("-------------------------------------------------------")
else:
    print("-------------------------------------------------------")
    print("Error querying the API, you may have overused it in a short period of time.")
    print("-------------------------------------------------------")


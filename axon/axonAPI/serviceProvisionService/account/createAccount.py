import requests
import json


axon_base_url = "https://rto.ptld.axon-networks.com/token"
endpoint = "/service-provision-service/service-provision/account"
token = input(
    "Enter token to create account: "
)  # "1cbe574e-6340-4338-bd9a-6db0f759ce13"

url = f"{ axon_base_url }{ endpoint }"

payload = json.dumps(
    {
        "externalId": "jose.python.testAccount",
        "name": "Jose Python Test Account",
        "description": "Python Test Account used for automation testing.",
    }
)

headers = {
    "Accept": "application/json",
    "x-api-key": token,
    "Content-Type": "application/json",
}

response = requests.post(url=url, headers=headers, data=payload)

print(f"Newly created account:\n{ response.text }")

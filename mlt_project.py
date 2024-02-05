import requests

url = "https://api.apilayer.com/odds/sports/cricket_big_bash/odds?regions=au"

payload = {}
headers= {
  "apikey": "bCr4ChpRxfQlNK4fNqNGjKra0OZ3IkPl"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)
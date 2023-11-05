import requests

url = "http://localhost:9696/predict"

client = {"month": ["12"], "weekday": ["12"], "day": ["12"], "latitude": ["55.46"],"longitude": ["26.00"]}

response = requests.post(url, json=client).json()

print(response)

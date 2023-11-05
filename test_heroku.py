import requests

url = "http://predict-atm-pressure-5bc65bbe7521.herokuapp.com/predict"

client = {"month": ["1"], "weekday": ["12"], "day": ["12"], "latitude": ["55.46"],"longitude": ["26.00"]}

response = requests.post(url, json=client).json()

print(response)

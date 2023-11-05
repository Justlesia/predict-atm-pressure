import requests

url = "http://localhost:9696/predict"

client = { "stat_num" :["53"], "year": ["2023"], "month": ["10"], "weekday": ["6"],	"day": ["15"],	"latitude": ["55.46"],
          "longitude": ["26.00"]}

response=requests.post(url, json=client).json()

print(response)
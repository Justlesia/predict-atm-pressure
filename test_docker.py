import requests

url = "http://localhost:9696/predict"

client = { "stat_num" :["1"], "code_quantity._id" : ["c07dc73f-feb0-4f78-aeb8-617ee8d4d09f"],
 "year": ["2024"], "month": ["1"],	"weekday": ["6"],	"day": ["15"],	"latitude": ["55.46"],
          "longitude": ["26.00"]}

response=requests.post(url, json=client).json()

print(response)
import requests

url = "http://localhost:9696/predict"

client = {"stat_num._id": ["f7636a52-2e03-43da-83d9-a70a8bb41f7b"],
 "stat_num"	:["51"], "code_quantity._id" : ["c07dc73f-feb0-4f78-aeb8-617ee8d4d09f"],
 "year": ["2023"], "month": ["11"],	"weekday": ["1"],	"day": ["15"],	"latitude": ["55.46"],
          "longitude": ["26.00"]}

response=requests.post(url, json=client).json()

print(response)
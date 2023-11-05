import requests

url = "http://predict-atm-pressure-5bc65bbe7521.herokuapp.com/predict"

client = { "stat_num" :["55"], "code_quantity._id" : ["c07dc73f-feb0-4f78-aeb8-617ee8d4d09f"],
 "year": ["2023"], "month": ["01"],	"weekday": ["6"],	"day": ["15"],	"latitude": ["55.46"],
          "longitude": ["26.00"]}

response=requests.post(url, json=client).json()

print(response)
client = {"stat_num._id": "f7636a52-2e03-43da-83d9-a70a8bb41f7b",
 "stat_num"	:"51", "code_quantity._id" : "c07dc73f-feb0-4f78-aeb8-617ee8d4d09f",
 "year": "2023", "month": "11",	"weekday": "1",	"day": "15",	"latitude": "55.46",	"longitude": "26.00"}

import pickle
from flask import Flask
from flask import request
from flask import jsonify


with open('model.bin', 'rb') as f_in:
    dv, scaler, model = pickle.load(f_in)

client[['latitude','longitude']] = scaler.transform(asarray(client[['latitude','longitude']]))

val_test = client.to_dict(orient='records')
X = dv.transform([val_test])

y_pred = model.predict(X)

print(y_pred)
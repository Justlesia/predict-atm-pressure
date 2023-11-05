#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from numpy import asarray
import pickle
from flask import Flask
from flask import request
from flask import jsonify

with open('model.bin', 'rb') as f_in:
    model = pickle.load(f_in)

with open('scaler.bin', 'rb') as f_in:
    scaler = pickle.load(f_in)

app = Flask('app')


@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    client = pd.DataFrame.from_dict(client)
    client[['latitude', 'longitude']] = scaler.transform(asarray(client[['latitude', 'longitude']]))

    y_pred = model.predict(client)

    result = {
        'atm.pressure': int(y_pred)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

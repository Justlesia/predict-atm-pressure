#!/usr/bin/env python
# coding: utf-8
 
# https://data.gov.lt/datasets/500/

import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction import DictVectorizer
from numpy import asarray

data_averages = pd.read_csv('datasets/Averages.csv', sep=',',decimal='.')
data_quantity = pd.read_csv('datasets/Quantity.csv', sep=',',decimal='.')
data_quantity_units = pd.read_csv('datasets/QuantityUnits.csv', sep=',',decimal='.')
data_station = pd.read_csv('datasets/Station.csv', sep=',',decimal='.')

data = data_averages.merge(data_quantity_units,how='left', on = 'code_combi')

data.groupby(by="code_unit._id", dropna=False)['lvalue'].mean()

data['datetime'] = pd.to_datetime(data.ldatetime)
data['year'] = data.datetime.dt.year
data['month'] = data.datetime.dt.month
data['weekday'] = data.datetime.dt.weekday
data['day'] = data.datetime.dt.day
data = data[data['year']== 2023]
data =data[data['code_unit._id'] == '67461e7c-506e-430a-8962-cd25ebed54da']
d_q = data_quantity[data_quantity['code_unit._id'] == '67461e7c-506e-430a-8962-cd25ebed54da'] 

data = data.merge(d_q,how='left', on = 'code_unit._id')
data_station['stat_num._id'] = data_station['_id']
data = data.merge(data_station,how='left', on = 'stat_num._id', suffixes=('_xx', '_yy'))
data = data[['lvalue','stat_num','code_quantity._id','year','month','weekday','day','latitude','longitude']]

data = data.drop_duplicates()

#выделим таргет
features, target = data.drop(['lvalue'], axis=1), data['lvalue']
features = features.fillna(0)

scaler = MinMaxScaler()

scaler.fit(asarray(features[['latitude','longitude']]))

features[['latitude','longitude']] = scaler.transform(asarray(features[['latitude','longitude']]))

# In[61]:
dicts = features.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)

model = GradientBoostingRegressor(learning_rate = 0.2, max_depth = 12)
model.fit(X, target)

with open('model.bin', 'wb') as f_out:
    pickle.dump(model, f_out)

with open('scaler.bin', 'wb') as f_out:
    pickle.dump(scaler, f_out)

with open('dv.bin', 'wb') as f_out:
    pickle.dump(dv, f_out)



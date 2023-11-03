# Project:  Air quality data. Environmental and climate monitoring.
# Atmosfer pressure. Regression model.
``` 
Artificial Intelligence  
Domain             : Regression
Sub-Domain         : Time series 
Architectures      : GradientBoostingRegressor
Application        : Meteological domain
```

### Description of data

The system of automatic state ambient air monitoring stations in Lithuania consists of 14 urban air quality monitoring stations operating in Vilnius, Kaunas, Klaipėda, Šiauliai, Panevėžys, Jonava, Kėdainiai, Naujoji Akmenė and Mažeikiai and 3 integrated monitoring stations operating in Aukštaitija, Žemaitija and Dzūkija National Parks.

Concentrations of the following pollutants are measured at automatic air quality monitoring stations: particulate matter PM10, fine particulate matter PM2.5, nitrogen oxides (NO2, NOx, NO), sulfur dioxide (SO2), carbon monoxide (CO), ozone (O3), benzene, mercury.
The tests and measurements shall be carried out in accordance with the requirements of Directives 2004/107/EC of the European Parliament and of the Council relating to arsenic, cadmium, mercury, nickel and polycyclic aromatic hydrocarbons in ambient air and 2008/50/EC on ambient air quality and cleaner air for Europe.

We will look at Atmosfer pressure measurements.

The data consists of files obtained from different sources(https://data.gov.lt/datasets/500/ ):

* Averages.csv - data air monitoring (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Averages/:format/csv)
* Quantity.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Quantity/:format/csv)
* QuantityUnits.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits/:format/csv)
* Station.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Station/:format/csv)

## Metrics of the Final Model
```
Final Model             : model.bin
Final DictVectorizer    : dv.bin
Final MinMaxScaler      : scaler.bin
MAE:                    : Val - 4,  Test - 7 
``` 
## Tools / Libraries
```
Languages               : Python
Tools/IDE               : Anaconda
Libraries               : Keras, TensorFlow
Virtual Environment     : pipenv
```

## Scripts and Notebook:
```
Notebook                : [https://github.com/Justlesia/predict-atm-pressure/blob/main/notebook.ipynb]
Predict Script          : [https://github.com/Justlesia/predict-atm-pressure/blob/main/predict.py]
Train Script            : [https://github.com/Justlesia/predict-atm-pressure/blob/main/train.py]
Test Script             : [https://github.com/Justlesia/predict-atm-pressure/blob/main/test.py]

```

## Run the Model as is  
Steps to run the scripts/notebooks as is:

### Using Docker 
 
   1. Clone the repo by running the following command:
   ```
   git clone https://github.com/Justlesia/predict-atm-pressure.git
   ```
   
   1. Download data into the ./datasets:

   (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Averages/:format/csv)
   (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Quantity/:format/csv)
   (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits/:format/csv)
   (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Station/:format/csv)
      
   2. Build and run the application using the commands:
      ```
      docker build -t predict . 
      docker run -it -p 9696:9696 predict:latest 
      ```
      
   3. Open another terminal/prompt and run predict_test.py  
      ``` 
      python predict_test.py (To test the prediction service)
      ```
      If the prediction services gives prediction, then it means the docker container is working.
      
## Deployment using AWS Lambda, AWS ECR and AWS API Gatway
   1. Go to ```AWS Lambda folder``` in the repository and type the following commands. The `Dockerfile` in the folder will be used to create a docker image.
      ```
      docker build -t cervical_fracture_model .
      docker run -it --rm -p 8080:8080 cervical_fracture_model:latest
      ```
   
   2. To test if the docker container was build properly and running, go to the lambda_predict_test.py and uncomment the 1st url variable and comment the 2nd url variable         and save the file with the changes.
      ```
      python lambda_predict_test.py
      ```
  
   3. Once it is confirmed the model is giving out the predictions from the container, go back to lambda_predict_test.py and comment the 1st url variable and uncomment the       2nd one and save the file. Also, stop the docker container.  This container will be uploaded to AWS ECR which will be then used by AWS Lambda functions to create a         AWS Lambda functions prediction service with the help as AWS API gateway. In order to achieve this, I followed the steps described on
      ```
      https://github.com/MuhammadAwon/ml-engineering/tree/main/09-serverless and ML Zoomcamp video recordings
      ```
      
   4. The working of the AWS Lambda functions with AWS API gateway will be confirmed when the 2nd url variable in lambda_predict_test.py is used as the url for requesting the prediction service and returns a prediction after running the following command.
      ```
      python lambda_predict_test.py 
      ``` 
      Simply put, if the prediction is returned  after step 3 is completed and lambda_predict_test.py is run, it means we uploaded the container and configured it to work with the other AWS services(AWS Lambda Functions and AWS API Gateway) correctly. Therefore, it is providing us with the prediction service.
      
      Screenshot of the service on AWS Lambda Functions: 
     ![Screenshot of the lambda function](https://user-images.githubusercontent.com/108292818/209393198-e5b82d5c-03d2-4b55-8bdf-0e038b425e5c.PNG)

      Prediction from the service when 2nd url variable(lambda-rest-api endpoint in the file lambda_predict_test.py) was used to test the deployment and the model.  
     ![Screenshot of the AWS lambda function working](https://user-images.githubusercontent.com/108292818/209398516-6cf1f486-c294-4629-be72-c906d4566c4b.PNG)

   
   

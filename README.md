# Project: Atmosfer pressure. Regression model.
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

We will loo at Atmosfer pressure measurements.

The data consists of files obtained from different sources:

* Averages.csv - data air monitoring (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Averages/:format/csv)
* Quantity.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Quantity/:format/csv)
* QuantityUnits.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits/:format/csv)
* Station.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Station/:format/csv)





## Dataset Details
```
Dataset Name       : Air quality data
Dataset Category       : Environmental and climate monitoring
Dataset Link       : [https://data.gov.lt/datasets/500/](https://data.gov.lt/datasets/500/)
Number : 
```

## Metrics of the Final Model
```
Final Model             : https://github.com/praveenbalijepalli/mlzoomcamp-capstone-1/blob/main/cerv_fracture_model.h5
Final TFlite Model      : https://github.com/praveenbalijepalli/mlzoomcamp-capstone-1/blob/main/cerv_fracture_model.tflite
MAE:                    : Val - 4,  Test - 7 
```


## Download the data in the ./datatset if needed
* Averages.csv - data air monitoring (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Averages/:format/csv)
* Quantity.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Quantity/:format/csv)
* QuantityUnits.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits/:format/csv)
* Station.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Station/:format/csv)


 
## Sample Input and Output

In the predict_test.py file, replace the data variable with the following:

1. Sample Input:
   ```
   data = {'url':'https://raw.githubusercontent.com/praveenbalijepalli/mlzoomcamp-capstone-1/main/sample%20images%20for%20testing/fracture.png'}
   ```

   Sample Output:
   ```
   {'Predict Probability': '0.06067303', 'Prediction': 'fracture'}
   ```
   
   
 2. Sample Input:
    ```
    data = {'url':'https://raw.githubusercontent.com/praveenbalijepalli/mlzoomcamp-capstone-1/main/sample%20images%20for%20testing/normal.png'}
    ```

    Sample Output:
    ```
    {'Predict Probability': '0.7252521', 'Prediction': 'normal'}
    ```
 
## Tools / Libraries
```
Languages               : Python
Tools/IDE               : Anaconda
Libraries               : Keras, TensorFlow
Virtual Environment     : pipenv
```

## Scripts
```
Train Script            : https://github.com/praveenbalijepalli/mlzoomcamp-capstone-1/blob/main/train.py
Keras to TFlite Script  : https://github.com/praveenbalijepalli/mlzoomcamp-capstone-1/blob/main/convert_keras_to_tflite.py
Predict Script          : https://github.com/praveenbalijepalli/mlzoomcamp-capstone-1/blob/main/predict_flask.py
Predict Test Script     : https://github.com/praveenbalijepalli/mlzoomcamp-capstone-1/blob/main/predict_test.py
```

## Run the Model as is  
Steps to run the scripts/notebooks as is:

1. Clone the repo by running the following command:
   ```
   git clone https://github.com/praveenbalijepalli/mlzoomcamp-capstone-1.git
   ```
2. Open a terminal or command prompt and change directory to the folder where this project is cloned.

3. Run the following command to activate the virtual environment for the project:
   ```
   pipenv shell
   ```

   In case, pipenv is not installed in your system, to install pipenv and to activate the virtual environment for the project, type the following commands:
   ```
   pip install pipenv 
   pipenv shell (in the project folder)
   ``` 
4.  To install the files and dependencies related to the project, run the following in the folder containing Pipfile/Pipfile.lock
    ```
    pipenv install
    ```
5.  To run the scripts do the following:

    a. To train the the model and save it using train.py script, run the following command in the terminal/prompt.
       ```
       python train.py (To train and save the model)
       ```
       
    b. Run predict_flask.py using python in a terminal/prompt.
       ```
       python predict_flask.py (To start the prediction service)
       ```
       
    c. Open another terminal/prompt and run predict_test.py.
       ```
       python predict_test.py (To test the prediction service)
       ```


## Model as a web service 

### Using Waitress  
   
   1. Follow the steps mentioned above from 1 to 4, if you haven't already completed them.
   
   2. To run the prediction service offered by predict_flask.py using waitress, type the following command
      ```
      waitress-serve --listen=0.0.0.0:9696 predict_flask:app (This will keep the running the prediction service)
      ```
      
   3. Open another terminal/prompt and run predict_test.py
      ```
      python predict_test.py (To test the prediction service)
      ``` 
      
 ### Using Docker 
 
   1. Clone the directory into you work space.
   
   2. Open predict_flask.py. Go to the part of the chart where libraries are imported. 
      ```
      Uncomment:  import tflite_runtime.interpreter as tflite  and 
      Comment:    import tensorflow.lite as tflite
      ```
      Save the changes to the file. This change is temporary. 
      Once we build run our docker image and test our predictions and get them right, we will change it back
      
   2. Build and run the application using the commands:
      ```
      docker build -t zoomcamp-capstone-1 .
      docker run -it --rm -p 9696:9696 zoomcamp-capstone-1  (This will keep the running the prediction service from the docker container)
      ```
      
   3. Open another terminal/prompt and run predict_test.py  
      ``` 
      python predict_test.py (To test the prediction service)
      ```
      If the prediction services gives prediction, then it means the docker container is working.
      
   4. Open predict_flask.py. Go to the part of the chart where libraries are imported. 
      ```  
      Comment:     import tflite_runtime.interpreter as tflite  and 
      Uncomment:   import tensorflow.lite as tflite
      ```
      Save the changes to the file.
 
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

   
   

# Fixed Route  Arrival Time Prediction

### UCI Data Science Capstone Capstone

### Julian Freedberg, Jullia Bautista, Shibo Tang

## Project Description

In order to facilitate travel and alleviate traffic pressure, more and more people choose to take public buses as a mode of transportation. As people's demand for buses gradually increases, improving high-quality service has become the most concerning issue of the bus service system. For our project objective, our goal is to implement and evaluate various approaches for stop arrival time prediction for fixed route bus systems and find out which model has the highest accuracy. Accurate bus arrival time predictions is a key component of rider satisfaction with bus service. We believe that by predicting the arrival time, passengers can easily manage their time and daily schedule.

SVM (support vector machines), NN (neural networks), and linear regression are the three models that have the most effect in this field, and our main proposal is to figure out which model has the best performance with lower errors by comparing with the data from AC transit (a large transit agency that provides bus service to Alameda and Contra Costa counties in the Bay Area) to test the accuracy. For our available data resources, we have historical bus arrival times and predictions data which we collected from AC Transit API, General Transit Feed Specification (GTFS) real time (RT) feed and the GTFS static files. GTFS-Real time feed that is updated continuously with operational vehicle information like the vehicle location, speed, next stop, occupancy status, the timestamp, vehicle speed, vehicle bearing, and the trip. GTFS static is a series of csv files containing schedule information like the stop locations and identifiers, as well as the scheduled arrival time which we will use to see whether a vehicle has arrived at a stop.


Below is the code for every aspect of our project.

## File Descriptions

- Data Cleaning.Rmd: This file takes in raw data from GTFS RT and GTFS Static and conducts the data cleaning and processing procedures and implements the data inclusion criterion.

- Linear Modeling: This file takes us through the modeling and cross validation steps for the linear model

- going_backwards.cpp: This file is used to correct a data quality issue where a bus will accidentally think its going to the next stop when still stopped its original stop. It is used in the data cleaning script via Rcpp

- identify_trips.cpp: This file creates a unique service ID that says what time period a trip occured. This is important so that we match the correct arrival time with the correct stop and trip

- data/route_800.csv: This file is a sample of the wrangled and cleaned dataset for route 800

- model2.pth: This file is the trained nearal network model

- NN-modeling.ipynb: This file contains the code for the neural network structure and visualization (Distribution of Accuracy & confusion matrix)

- stats170svm800.ipynb: This file contains the code to model the support vector machines.

- svm.joblib: This file contains the trained support vector machine model.

- gtfs-realtime-pb2.py: Reference file for to parse GTFS realtime protobuffer format

- pull-vehicle-locations.py & main.py: Pulls GTFS RT data from AC Transit API and converts it to pandas dataframe, inserts to local database
 
## Notebooks to Run

- Linear Modeling Demo.Rmd This takes you through the linear modeling procecures for route 800. This notebook should install all required dependencies

- SVM-NN Demo.ipynb: Dependencies: pytorch, sklearn, matplotlib, seaborn, pandas, and numpy
              
     - This file contains the support vector machine and neural networks demo. It uses both the trained models provided in svm.joblib and model2.pth, and predicts the delay of route 800.

## Pre Run Notebooks

- project-R.html: Pre run version of "Linear Modeling Demo.Rmd"

- project-python.html: Pre run version of "SVM/NN Demo.ipynb"

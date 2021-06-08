# Arrival Time Prediction


Below is the code for every aspect of our project.

## File Descriptions

- Data Cleaning.Rmd: This file takes in raw data from GTFS RT and GTFS Static and conducts the data cleaning and processing procedures and implements the data inclusion criterion.

- Linear Modeling: This file takes us through the modeling and cross validation steps for the linear model

- going_backwards.cpp: This file is used to correct a data quality issue where a bus will accidentally think its going to the next stop when still stopped its original stop. It is used in the data cleaning script via Rcpp

- identify_trips.cpp: This file creates a unique service ID that says what time period a trip occured. This is important so that we match the correct arrival time with the correct stop and trip

- data/route_800.csv: This file is a sample of the wrangled and cleaned dataset for route 800

- model2.pth: This file is the trained nearal network model

- NN-modeling.ipynb: This file contains the code for the neural network structure

- stats170svm800.ipynb: This file contains the code to model the support vector machines.

- svm.joblib: This file contains the trained support vector machine model.
 
## Notebooks to Run

- Linear Modeling Demo.Rmd This takes you through the linear modeling procecures for route 800. This notebook should install all required dependencies

- SVM/NN Notebook: Dependencies: pytorch, sklearn, matplotlib, seaborn, pandas, and numpy
              
     - SVMDemo.ipynb: This file contains the support vector machine demo. It uses the trained model provided in svm.joblib and predicts the delay of route 800.

## Pre Run Notebooks

- project-R.html: Pre run version of "Linear Modeling Demo.Rmd"

- SVMDemo.html: Pre run version of "SVMDemo.ipynb"

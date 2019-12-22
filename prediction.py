import numpy as np
import pandas as pd
from sklearn.externals import joblib
import csv
import datetime
from math import sqrt
from sklearn.tree import DecisionTreeRegressor
from datetime import timedelta
from training import training


def menu():
    print("*" *58)
    print("-"*5 + " Do you like to predict weather of another date " + "-" * 5)
    print("\n")
    print("1. Yes.")
    print("2. No.")
    print("\n")

    option = input("Selcted Option: ")

    while True:
        if option == '1':
            prediction()
        else:
            print("Thank you")
        break
    

def prediction():
    tree_model = joblib.load('weather_predictor.pkl')

    print("-" * 58)
    print("Enter the details of the date you would like to predict")
    print("\n")
    fy = input("Enter Year: ")
    fm = input("Enter Month (00): ")
    fd = input("Enter Day (00): ")

    Id = str(fm) + str(fd)
    
    date = [[Id, (str(int(Id) + 1)), (Id)]
    ]
    temp = tree_model.predict(date)[0]

    print("-" * 58)
    print("\nThe temperature is estimated to be: " + str(temp) + " degree celcius" "\n")
    print("-" * 58)
    menu()

training()
prediction()


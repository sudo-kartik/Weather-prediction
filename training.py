import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.externals import joblib
import csv
from data_pre_processing import new_array


def training():
    col_present = ['Fran Datum Tid (UTC)', 'till', 'day', 'temperature', 'Kvalitet', 'Tidsutsnitt:', 'Unnamed: 5']
    
    col_used = ['Fran Datum Tid (UTC)', 'till', 'day']

    df1 = pd.read_csv("data1.csv", sep=';', skiprows=3607, names=col_present)
    df2 = pd.read_csv("data2.csv", sep=';', skiprows=15, names=col_present)

    df1 = df2.append(df1)
    X = df1.drop(['temperature','Tidsutsnitt:', 'Kvalitet', 'Unnamed: 5'], axis = 1)
    new_array(X)

    y = df1['temperature']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=123)

    tree_model = DecisionTreeRegressor()

    tree_model.fit(X_train, y_train)
    joblib.dump(tree_model, 'weather_predictor.pkl')
    print("-" * 58)
    print("\nReady\n")
    print("-" * 58)

    
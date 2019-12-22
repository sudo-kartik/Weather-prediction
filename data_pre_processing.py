import numpy as np
import pandas as pd
import datetime
from datetime import timedelta
from math import sqrt
import csv


col_present = [
    'Fran Datum Tid (UTC)', 'till', 'day', 'temperature', 'Kvalitet', 'Tidsutsnitt:', 'Unnamed: 5'
    ]
col_used = [
        'Fran Datum Tid (UTC)', 'till', 'day'
    ]

def num_val(arr, title):
    new_arr = []
    for date in arr[title]:
        new_date = curr_d(date)
        new_arr.append(new_date)
    arr[title] = new_arr

def new_array(arr):
    for name in col_used:
        num_val(arr, name)

def curr_d(date):
    new_date = date.split(' ')
    new_date = new_date[0]
    new_date = new_date.split('-')
    new_number = ''
    first = True
    for number in new_date:
        if first:
            first = False
        else:
            new_number = new_number + number
    return new_number


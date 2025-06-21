import numpy as nps
import pandas as pd
from flask import Flask, request, jsonify
import pickle
import os
from google.cloud import storage

def preprocess_data(df):
    df = df.fillna(df.mode().iloc[0])
    df = df.drop_duplicates()
    return df

def load_model():
    file_path = "../artifact/trained_model.pkl"
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

def preprocess(input_json):
    try:
        df = pd.DataFrame(input_json, index=[0])
        x = preprocess_data(df)
        return x
    
    except Exception as e:
        print("ERROR - PREPROCESS")
    
def predict(input_json):
    model = load_model()
    try : 
        df_preprocessed = preprocess(input_json)
        y_predictions = model.predict(df_preprocessed)
        response = {'predictions': list(y_predictions)}
        return response
    
    except Exception as e:
        print("ERROR - PREDICT")

input_data = {
        "holiday": 0,
        "weekday": 6,
        "workingday": 0,
        "weathersit": 2,
        "temp": 0.344167,
        "atemp": 0.363625,
        "hum": 0.805833,
        "windspeed": 0.160446,
        "casual": 331,
        "registered": 654
    }

print(predict(input_data))
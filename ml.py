import pandas as pd
import numpy as np

def trainingModel():
    train_data = pd.read_csv('database/train_data.csv')
    test_data = pd.read_csv('database/test_data.csv')
    model = "INSERT MODEL HERE"
    return model

def predictInput(data):
    model = trainingModel()
    # prediction = model.predict(data.Tweet)
    # return prediction
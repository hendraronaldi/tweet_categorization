import pandas as pd
import numpy as np
import pickle

from preprocess import preProcess

def trainingModel():
    train_data = pd.read_csv('database/train_data.csv')
    test_data = pd.read_csv('database/test_data.csv')
    model = "INSERT MODEL HERE"
    # train model

    # save model
    model_filename = 'final_model.sav'
    pickle.dump(model, open(model_filename, 'wb'))

def predictInput(data):
    model_filename = 'final_model.sav'
    # model = pickle.load(open(model_filename, 'rb'))
    # prediction = model.predict(data.Tweet)
    # return prediction
import pandas as pd
import numpy as np
import pickle
from xgboost import XGBClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from preprocess import preProcess

def trainingModel():
    # load data
    data = pd.read_excel("../Ica_Labelled Tweets (selesai).xlsx", index_col=None, sheet_name='tweets_text', skiprows=[0,1,2], na_values=['-', ' '])
    cleaned_data = preProcess(data)
    
    # train test split
    X = cleaned_data[['tweet']]
    y = cleaned_data[['label']]
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=42)

    # train model
    model = XGBClassifier()
    model.fit(X_train, y_train)

    # test model & evaluate predictions
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))

    # save model
    model_filename = 'final_model.sav'
    pickle.dump(model, open(model_filename, 'wb'))
import pickle

def predictInput(data):
    model_filename = 'final_model.sav'
    model = pickle.load(open(model_filename, 'rb'))
    predictions = model.predict(data.tweet)
    data.label = predictions
    return data
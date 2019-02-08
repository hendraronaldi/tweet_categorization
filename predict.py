import pickle
import pandas as pd

def predictInput(tweets):
    gpc = pickle.load(open('gpc_model.sav', 'rb'))
    dt = pickle.load(open('dt_model.sav', 'rb'))
    mlp = pickle.load(open('mlp_model.sav', 'rb'))
    y_pred_gpc = gpc.predict(tweets)
    y_pred_dt = dt.predict(tweets)
    y_pred_mlp = mlp.predict(tweets)
    predictions = {
        'gpc_pred': y_pred_gpc,
        'dt_pred': y_pred_dt,
        'mlp_pred': y_pred_mlp
    }
    data = pd.DataFrame(data=predictions)
    return data
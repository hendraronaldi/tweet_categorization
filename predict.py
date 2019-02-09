import pickle
import pandas as pd

def predictInput(tweets):
    # gpc = pickle.load(open('gpc_model.sav', 'rb'))
    dt = pickle.load(open('dt_model.sav', 'rb'), encoding='latin1')
    mlp = pickle.load(open('mlp_model.sav', 'rb'), encoding='latin1')
    # y_pred_gpc = gpc.predict(tweets)
    y_pred_dt = dt.predict(tweets)
    y_pred_dt = [y.decode('utf-8') for y in y_pred_dt]
    y_pred_mlp = mlp.predict(tweets)
    y_pred_mlp = [y.decode('utf-8') for y in y_pred_mlp]
    predictions = {
        # 'gpc_pred': y_pred_gpc,
        'dt_pred': y_pred_dt,
        'mlp_pred': y_pred_mlp
    }
    data = pd.DataFrame(data=predictions)
    return data
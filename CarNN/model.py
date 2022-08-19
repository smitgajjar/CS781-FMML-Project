import pickle
import sklearn
import joblib
import pandas as pd

def execute(X):
    f = open('examples/CarNN/mlp_model_carNN', 'rb')
    mlp_model = joblib.load(f)
    outputvalue = mlp_model.predict(pd.DataFrame([X]))
    return outputvalue[0]


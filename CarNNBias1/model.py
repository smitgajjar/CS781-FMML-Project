import pickle
import sklearn
import joblib
import pandas as pd

def execute(X):
    f = open('examples/CarNNBias1/mlp_model_carNNBias1DR', 'rb')
    mlp_model = joblib.load(f)
    # with open('examples/CarNNBias1/mlp_model_carNNBias1DR', 'rb') as fid:
    # gnb_loaded = cPickle.load(fid)
    outputvalue = mlp_model.predict(pd.DataFrame([X]))
    return outputvalue[0]

print(execute([2,	2,	0,	0,	2,	0]))


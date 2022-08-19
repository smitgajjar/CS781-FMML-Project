import pickle
import sklearn
import joblib
import pandas as pd

outputclasslist = ['acc', 'good', 'unacc', 'vgood']

def execute(X):
    f = open('examples/Car/clf_gini', 'rb')
    clf_gini = joblib.load(f)
    outputvalue = clf_gini.predict(pd.DataFrame([X]))
    index = outputclasslist.index(outputvalue)
    return index

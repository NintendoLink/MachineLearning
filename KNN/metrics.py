# python 3.6.4
# encoding: utf-8

import  numpy as np

def accuracy_score(y_predict,y_test):
    return np.sum(y_predict == y_test) / len(y_test)

def MAE(y,y_predict):
    return (np.array(y) - np.array(y_predict)).dot((np.array(y) - np.array(y_predict))) / len(y)

def RMSE(y,y_predict):
    return np.sqrt(MAE(y,y_predict))

def MAE(y,y_predict):
    np.sum(np.sqrt(np.array(y) - np.array(y_predict))) / len(y)
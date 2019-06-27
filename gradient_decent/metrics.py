# python 3.6.4
# encoding: utf-8

import  numpy as np

def accuracy_score(y_predict,y_test):
    return np.sum(y_predict == y_test) / len(y_test)

def mean_squared_error(y, y_predict):
    return (np.array(y) - np.array(y_predict)).dot((np.array(y) - np.array(y_predict))) / len(y)

def root_mean_squared_error(y, y_predict):
    return np.sqrt(mean_squared_error(y, y_predict))

def mean_abs_error(y, y_predict):
    return np.sum(np.absolute(np.array(y) - np.array(y_predict))) / len(y)

def r2_score(y, y_predict):
    return 1 - (mean_squared_error(y,y_predict) / np.var(y))


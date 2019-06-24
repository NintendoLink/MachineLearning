# python 3.6.4
# encoding: utf-8

import  numpy as np

def accuracy_score(y_predict,y_test):
    return np.sum(y_predict == y_test) / len(y_test)
# python 3.6.4
# encoding: utf-8

'''
    标准化函数
'''
import numpy as np
class StandScaler():

    def __init__(self):
        self.mean = None
        self.scale_ = None

    def fit(self,X):

        dim = len(X[0])
        self.mean = [np.mean(X[:,i])for i in range(dim)]
        self.scale_ = [np.std(X[:,i]) for i in range(dim)]

    def transform(self,X):
        X_std = [(X[:,i] - self.mean) / self.scale_ for i in range(len(0))]
        return X_std
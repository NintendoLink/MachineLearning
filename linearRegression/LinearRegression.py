# python 3.6.4
# encoding: utf-8

import  numpy as np
from metrics import r2_score
class LinearRegression():

    def __init__(self):
        self.coef_ = None
        self._theta = None
        self.interception_ = None

    def fit_normal(self,X_train,y):

        X_train = np.hstack([np.ones((len(X_train),1)),X_train])

        self._theta = np.linalg.inv((X_train.T).dot(X_train)).dot(X_train.T).dot(y)
        self.coef_ = self._theta[1:]
        self.interception_ = self._theta[0]

    def predict(self,X):
        X_b = np.hstack([np.ones((len(X),1)),X])
        return X_b.dot(self._theta)

    def score(self,X,y_true):
        y_predict = self.predict(X)
        return r2_score(y_true,y_predict)

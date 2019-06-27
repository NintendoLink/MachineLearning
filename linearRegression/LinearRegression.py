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

    def fit_gd(self,X_train,y_train,eta = 0.1,eplison = 1e-8,iter_num = 1e4):

        def J(theta,X_b,y):

            try:
                return np.sum((X_b.dot(theta) - y) ** 2)
            except:
                return 'inf'

        def dJ(theta,X_b,y):
            res = np.empty(len(theta))
            res[0] = np.sum((X_b.dot(theta) - y))
            for i in range(1,len(theta)):
                res[i] = (X_b.dot(theta) - y).dot(X_b[:,i])
            res = 2 * res /  len(theta)
            return res

        def gradient(X_b,y,init_theta):

            theta = init_theta
            iter =0
            while(iter < iter_num):
                last_theta = theta
                theta = theta - eta * dJ(theta,X_b,y)
                if(np.abs(J(theta,X_b,y) - J(last_theta,X_b,y))) < eplison:
                    break

                iter += 1

            return theta
        X_b = np.hstack([np.ones((len(X_train),1)),X_train])
        init_theta = np.ones(X_b.shape,1)

        theta = gradient(X_b,y_train)
        self._theta = theta
        self.coef_ = theta[1:]
        self.interception_ = theta[0]

        return self
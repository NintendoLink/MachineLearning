# python 3.6.4
# encoding: utf-8

import numpy as np
class PCA():

    def __init__(self,n_component):
        self.n_component = n_component
        self.X_history =[]
        self.component = []


    def fit(self,X):

        def demean(X):
            return X - np.mean(X,axis=0)

        def dorection(w):
            return w / np.linalg.norm(w)

        def J(w,X):
            return np.sum(X.dot(w) ** 2) / len(X)

        def dJ(w,X):
            return X.T.dot(X.dot(w)) * 2 / len(X)

        def gradient_ascent(init_w,X,iter_num = 1e4,eta = 0.01,eplison = 1e-8):

            w = dorection(init_w)
            iter = 0
            while iter < iter_num:
                last_w = w
                gradient = dJ(w,X)

                w = w + eta * gradient
                w = dorection(w)

                if np.abs(J(w,X) - J(last_w,X)) < eplison:
                    break
                iter += 1
            return w

        init_w = np.random.normal(size=X.shape[1])
        last_X = X
        last_w = init_w
        for i in range(self.n_component):
            w = gradient_ascent(last_w,last_X)
            X = last_X - last_X.dot(w).reshape(-1,1) * w

            self.X_history.append(X)
            self.component.append(w)
            last_X = X
            last_w = w
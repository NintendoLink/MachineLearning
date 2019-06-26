# python 3.6.4
# encoding: utf-8

import numpy as np
class SimpleLinearRegression():

    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self,x,y):

        self.a_ = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)
        self.b_ = np.mean(y) - self.a_ * np.mean(x)

    def predict(self,x):
        y_hat = self.a_ * x + self.b_
        return y_hat

class SimpleLinearRegression2():

    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self, x, y):
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        self.a_ = (x - x_mean).dot(y - y_mean) / (x - x_mean).dot(x - x_mean)
        self.b_ = y_mean - self.a_ * x_mean

    def predict(self,x):
        y_hat = self.a_ * x + self.b_
        return y_hat

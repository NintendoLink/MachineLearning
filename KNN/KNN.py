# python 3.6.4
# encoding: utf-8
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from collections import Counter
class KNNClassfier():

    def __init__(self,K):
        self.K = K

    def fit(self,X_train,y_train):
        self._X_train = X_train
        self._y_train = y_train

    def predict(self, X_predict):

        y_predict = [self._predict(x_predict) for x_predict  in X_predict]
        return np.array(y_predict)

    def _predict(self, x_predict):

        distances = [np.sqrt(np.sum((x_predict - x_train) ** 2)) for x_train in self._X_train]

        nearest = np.argsort(distances)

        top_K = [self._y_train[i] for i in nearest[:self.K]]

        vote = Counter(top_K)

        return vote.most_common(1)[0][0]

if __name__ == '__main__':
    X_train = [[3.3,2.3],
             [3.1,1.7],
             [1.3,3.3],
             [3.5,4.6],
             [2.2,2.8],
             [7.4,4.6],
             [5.7,3.5],
             [9.1,2.5],
             [7.7,3.4],
             [7.9,0.8]]

    y_train = [0,0,0,0,0,1,1,1,1,1]
    knn_clf = KNNClassfier(6)
    knn_clf.fit(X_train,y_train)
    print(knn_clf.predict(np.array([[8.0,3.3]])))
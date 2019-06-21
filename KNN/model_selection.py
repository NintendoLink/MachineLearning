# python 3.6.4
# encoding: utf-8

import  numpy as np

'''
    model selection
'''
def train_test_split(X,y,ratio,random_seed):

    if random_seed:
        np.random.seed(random_seed)

    shuffle_index = np.random.permutation(len(y))

    test_size = int(ratio * len(y))

    train_index = shuffle_index[test_size:]


    test_index= shuffle_index[:test_size]

    X_train = X[train_index]
    X_test = X[test_index]
    y_train = y[train_index]
    y_test = y[test_index]

    return X_train,X_test,y_train,y_test

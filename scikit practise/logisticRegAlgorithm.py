# import module part
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import pandas as pd
import seaborn as sns
from ggplot import *


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def h_of_theta(theta, X):
    transposed_theta = theta[:, None]
    return sigmoid(X.dot(transposed_theta))


def costFunction(theta, X, y, lamda):
    """ lamda for regularization parameter """
    m = len(y) * 1.0
    h_theta = h_of_theta(theta, X)

    regularized_item = (float(lamda) / 2) * theta ** 2
    cost_vector = y * np.log(h_theta) + (1 - y) * np.log(1 - h_theta)
    # theta 0 not to be regularized
    J = -sum(cost_vector) / m + sum(regularized_item[1:]) / m

    return J[0]


def gradient(theta, X, y, lamda):
    """ return the gradient of theta """
    m = len(y)
    h_theta = h_of_theta(theta, X)
    derivative_regularization_item = float(lamda) * theta / m
    grad = (h_theta - y).T.dot(X) / m + derivative_regularization_item.T
    grad[0][0] -= derivative_regularization_item[0]

    return np.ndarray.flatten(grad)


def predict(theta, X):
    h_theta = h_of_theta(theta, X)
    return np.round(h_theta)

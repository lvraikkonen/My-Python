# Adaline using Stochastic Gradient Descent
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.evaluate import plot_decision_regions

class AdalineSGD(object):

	def __init__(self, alpha=0.1, iter_num=50):
		self.alpha = alpha
		self.iter_num = iter_num

	def net_input(self, X):
		return np.dot(X, self.w_[1:]) + self.w_[0]

	def activation(self, X):
		return self.net_input(X)

	def predict(self, X):
		return np.where(self.activation(X) >= 0.0, 1, -1)

	def train(self, X, y, reinitialize_weights=True):
		if reinitialize_weights:
			self.w_ = np.zeros(1 + X.shape[1])
		self.cost_ = []

		for _ in range(self.iter_num):
			for xi, target in zip(X, y):
				output = self.net_input(xi)
				error = target - output
				self.w_[0] += self.alpha * error
				self.w_[1:] += self.alpha * xi.dot(error)
			cost = (y - self.activation(X) ** 2).sum() / 2.0
			self.cost_.append(cost)
		return self
		
		# Gradient Descent using whole dataset to calculate update
		# output = self.net_input(X)
		# errors = (y - output)
		# # update weights
		# self.w_[0] += self.alpha * errors.sum()
		# self.w_[1:] += self.alpha * X.T.dot(errors)
		# cost = (errors**2).sum() / 2.0
		# self.cost_.append(cost)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
# setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y=='Iris-setosa', -1, 1)
X = df.iloc[0:100, [0,2]].values

# standardize features
X_std = np.copy(X)
X_std[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
X_std[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()

ada = AdalineSGD(iter_num=15, alpha=0.01)

# shuffle data
np.random.seed(123)
idx = np.random.permutation(len(y))
X_shuffled, y_shuffled =  X_std[idx], y[idx]

# train and adaline and plot decision regions
ada.train(X_shuffled, y_shuffled)
plot_decision_regions(X_shuffled, y_shuffled, clf=ada)
plt.title('Adaline - Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.show()

plt.plot(range(1, len(ada.cost_)+1), ada.cost_, marker='o')
plt.xlabel('Iterations')
plt.ylabel('Sum-squared-error')
plt.show()

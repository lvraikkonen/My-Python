# Adaline using Stochastic Gradient Descent
import numpy as np
from numpy.random import seed
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.evaluate import plot_decision_regions

class AdalineSGD(object):

	def __init__(self, alpha=0.01, iter_num=10, shuffle=True, random_state=None):
		self.alpha = alpha
		self.iter_num = iter_num
		self.w_initialized = False
		self.shuffle = shuffle
		if random_state:
			seed(random_state)

	def _shuffle(self, X, y):
		r = np.random.permutation(len(y))
		return X[r], y[r]

	def _initialize_weights(self, m):
		self.w_ = np.zeros(1 + m)
		self.w_initialized = True

	def _update_weights(self, xi, target):
		output = self.net_input(xi)
		error = target - output
		self.w_[0] += self.alpha * error
		self.w_[1:] += self.alpha * xi.dot(error)
		cost = (error ** 2) / 2.0
		return cost

	def net_input(self, X):
		return np.dot(X, self.w_[1:]) + self.w_[0]

	def activation(self, X):
		return self.net_input(X)

	def predict(self, X):
		return np.where(self.activation(X) >= 0.0, 1, -1)

	def fit(self, X, y):
		self._initialize_weights(X.shape[1])
		self.cost_ = []
		for _ in range(self.iter_num):
			if self.shuffle:
				X, y = self._shuffle(X, y)
			cost = []
			for xi, target in zip(X, y):
				cost.append(self._update_weights(xi, target))
			avg_cost = sum(cost) / len(y)
			self.cost_.append(avg_cost)
		return self

	def partial_fit(self, X, y):
		"""Fit training data without reinitializing the weights"""
		if not self.w_initialized:
			self._initialize_weights(X.shape[1])
		if y.ravel().shape[0] > 1:
			for xi, target in zip(X, y):
				self._update_weights(xi, target)
		else:
			self._update_weights(X, y)
		return self

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

ada = AdalineSGD(iter_num=15, alpha=0.01, random_state=1)
ada.fit(X_std, y)

# # shuffle data
# np.random.seed(123)
# idx = np.random.permutation(len(y))
# X_shuffled, y_shuffled =  X_std[idx], y[idx]

# # train and adaline and plot decision regions
# ada.train(X_shuffled, y_shuffled)
plot_decision_regions(X_std, y, clf=ada)
plt.title('Adaline - Stochastic Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.show()

plt.plot(range(1, len(ada.cost_)+1), ada.cost_, marker='o')
plt.xlabel('Iterations')
plt.ylabel('Sum-squared-error')
plt.show()

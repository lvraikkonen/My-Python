# Perceptron
# This Perceptron basic concept
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.evaluate import plot_decision_regions

class Perceptron(object):

	def __init__(self, alpha=0.01, iter_num=50):
		self.alpha = alpha
		self.iter_num = iter_num

	def net_input(self, X):
		return np.dot(X, self.w_[1:]) + self.w_[0]

	def predict(self, X):
		return np.where(self.net_input(X) >= 0.0, 1, -1)

	def train(self, X, y):
		self.w_ = np.zeros(1 + X.shape[1])
		self.errors_ = []

		for _ in range(self.iter_num):
			errors = 0
			for xi, target in zip(X, y):
				# update weights
				delta = self.alpha * (target - self.predict(xi))
				self.w_[1:] += delta * xi
				self.w_[0] += delta * 1 # x0=1
				errors += int(delta != 0.0)
			self.errors_.append(errors)
		return self


df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
# setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y=='Iris-setosa', -1, 1)
X = df.iloc[0:100, [0,2]].values

ppn = Perceptron(alpha=0.1, iter_num=10)

ppn.train(X, y)
print('Weights: %s' % ppn.w_)
plot_decision_regions(X, y, clf=ppn)
plt.title('Perceptron')
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.show()


# plot errors
plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
plt.xlabel('Iterations')
plt.ylabel('Missclassifications')
plt.show()

# Demo of Scrappy K Nearest Neighbor Classifier
# See Josh Gordon's 'Writing our first Classifier' video
# https://youtu.be/AoeEHqVSNOw

import random

class RandomGuessClassifier():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = random.choice(self.y_train)
            predictions.append(label)

        return predictions

# Load the iris dataset, which describes three types of iris flowers
# http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

# Video says to do the following...
# from sklearn.cross_validation import train_test_split

# ...but cross_validation is deprecated, use model_selection module instead:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

my_classifier = RandomGuessClassifier()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print( accuracy_score(y_test, predictions) )

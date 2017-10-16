# Demo of Scrappy K Nearest Neighbor Classifier
# See Josh Gordon's 'Writing our first Classifier' video
# https://youtu.be/AoeEHqVSNOw

from scipy.spatial import distance
def euc(a,b):
    return distance.euclidean(a,b)

class ScrappyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)

        return predictions

    def closest(self,row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i

        return self.y_train[best_index]


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

from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print( accuracy_score(y_test, predictions) )

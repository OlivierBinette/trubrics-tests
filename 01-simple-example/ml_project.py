# Adapted from https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html
# License: BSD 3 clause

# Standard scientific Python imports
import matplotlib.pyplot as plt
import pandas as pd

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from trubrics.context import DataContext

# Load the digits dataset
digits = datasets.load_digits()

# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
model_name = "My model"
model_version = "1.0"
clf = svm.SVC(gamma=0.001)

# Split data into 50% train and 50% test subsets
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
datacontext = DataContext(
    name="digits dataset",
    version="July 1998",
    testing_data=pd.concat(
        {"X": pd.DataFrame(X_test), "y": pd.DataFrame(y_test)}, axis=1
    ),
    target="y",
)

# Learn the digits on the train subset
clf.fit(X_train, y_train)

# Predict the value of the digit on the test subset
predicted = clf.predict(X_test)

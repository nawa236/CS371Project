import pandas as pd 
import numpy as np
import csv 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn import tree
from sklearn.neural_network import MLPClassifier


df = pd.read_csv("ips.csv", header=None)
# You might not need this next line if you do not care about losing information about flow_id etc. All you actually need to
# feed your machine learning model are features and output label.
columns_list = ['flow_id', 'proto', 'sport', 'dport', 'min', 'max', 'average', 'stddev', 'label']
df.columns = columns_list
features = ['proto', 'sport', 'dport', 'min', 'max', 'average', 'stddev']

X = df[features]
y = df['label']

acc_scores = 0
for i in range(0, 10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

    #Decision Trees
    clf1 = tree.DecisionTreeClassifier()
    clf1.fit(X_train, y_train)

    # Neural network (MultiPerceptron Classifier)
    clf2 = MLPClassifier()
    clf2.fit(X_train, y_train)

    #SVM's
    clf3 = SVC(gamma='auto')     #SVC USE THIS
    clf4 = LinearSVC()  #Linear SVC
    clf3.fit(X_train, y_train) 
    clf4.fit(X_train, y_train)

    #here you are supposed to calculate the evaluation measures indicated in the project proposal (accuracy, F-score etc)
    result1 = clf1.score(X_test, y_test)  #accuracy score
    result2 = clf2.score(X_test, y_test)
    result3 = clf3.score(X_test, y_test)
    result4 = clf4.score(X_test, y_test)
    print result1, result2, result3, result4


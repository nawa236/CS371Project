import pandas as pd 
import numpy as np
import csv 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix


#df = pd.read_csv("ips.csv", header=None)
df = pd.read_csv("ips.csv")
# You might not need this next line if you do not care about losing information about flow_id etc. All you actually need to
# feed your machine learning model are features and output label.
columns_list = ['flow_id', 'proto', 'sport', 'dport', 'min', 'max', 'average', 'stddev', 'label']
df.columns = columns_list
features = ['proto', 'sport', 'dport', 'min', 'max', 'average', 'stddev']

x = df[features]
y = df['label']

acc_scores = 0
for i in range(0, 10):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

    #Decision Trees
    clf1 = tree.DecisionTreeClassifier()
    clf1.fit(X_train, y_train)
    
    y1_pred = clf1.predict(X_test)
    
    DT_accuracy_arr = []
    DT_f1score_arr = []
    DT_precision_arr = []
    DT_recall_arr = []
    #print (classification_report(y_test, y_pred, target_names=x))

    DT_accuracy_arr.append(accuracy_score(y_test, y1_pred))
    DT_precision_arr.append(precision_score(y_test, y1_pred, average='weighted'))
    DT_recall_arr.append(recall_score(y_test, y1_pred, average='weighted'))
    DT_f1score_arr.append(f1_score(y_test, y1_pred, average='weighted'))
    
    # Neural network (MultiPerceptron Classifier)
    clf2 = MLPClassifier()
    clf2.fit(X_train, y_train)
    
    y2_pred = clf2.predict(X_test)

    NN_accuracy_arr = []
    NN_f1score_arr = []
    NN_precision_arr = []
    NN_recall_arr = [] 
   
    NN_accuracy_arr.append(accuracy_score(y_test, y2_pred))
    NN_precision_arr.append(precision_score(y_test, y2_pred, average='weighted'))
    NN_recall_arr.append(recall_score(y_test, y2_pred, average='weighted'))
    NN_f1score_arr.append(f1_score(y_test, y2_pred, average='weighted'))

    #SVM's
    clf3 = SVC(gamma='auto')     #SVC USE THIS
    #clf3 = LinearSVC()  #Linear SVC
    clf3.fit(X_train, y_train) 
    
    y3_pred = clf3.predict(X_test)

    SVC_accuracy_arr = []
    SVC_f1score_arr = []
    SVC_precision_arr = []
    SVC_recall_arr = []

    SVC_accuracy_arr.append(accuracy_score(y_test, y3_pred))
    SVC_precision_arr.append(precision_score(y_test, y3_pred, average='weighted'))
    SVC_recall_arr.append(recall_score(y_test, y3_pred, average='weighted'))
    SVC_f1score_arr.append(f1_score(y_test, y3_pred, average='weighted'))
    

with open("scores.csv", "a") as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',', quotechar ='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow([DT_accuracy_arr[0], DT_f1score_arr[0], DT_precision_arr[0], DT_recall_arr[0], NN_accuracy_arr[0], NN_f1score_arr[0], NN_precision_arr[0], NN_recall_arr[0], SVC_accuracy_arr[0], SVC_f1score_arr[0], SVC_precision_arr[0], SVC_recall_arr[0]])

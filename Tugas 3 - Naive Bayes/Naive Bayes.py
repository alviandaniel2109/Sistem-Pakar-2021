from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

#Load dataset
cancer = datasets.load_breast_cancer()

# print the names of the 13 feature
print("Features: ", cancer.feature_names)
print("")
# print the label type of wine(class_0, class_1, class_2)
print("Labels: ", cancer.target_names)
print("")

# print data(feature)shape
cancer.data.shape

print (cancer.data[0:5])

# print the wine labels (0:Class_0, 1:class_2, 2:class_2)
print (cancer.target)

# Import train_test_split function


# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=1000) # 70% training and 30% test


#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
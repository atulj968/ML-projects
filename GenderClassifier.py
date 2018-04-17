from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import numpy as np


#comparing results of 4 classifiers from sklearn package

#[height, weight, show size](Dummy Data)
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
		[166, 65, 40], [190, 90, 47], [175,64,39], [177,70,40],[171,75,42],
		[181,85,43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male',
		'male', 'female', 'female', 'male']		

clf = tree.DecisionTreeClassifier()
knn_clf = KNeighborsClassifier()
random_fc = RandomForestClassifier()
gaussian_Nbc = GaussianNB()

clf = clf.fit(X,Y)
knn_clf = knn_clf.fit(X,Y)
random_fc = random_fc.fit(X,Y)
gaussian_Nbc = gaussian_Nbc.fit(X, Y)

prediction = clf.predict([[190, 70, 43]])		
knn_prediction = knn_clf.predict([[190, 70, 43]])
random_fc_prediction = random_fc.predict([[190,70,43]])
gaussian_Nbc_prediction = gaussian_Nbc.predict([[190,70,43]])

# The best classifier from DecissionTree, KNN, RandomForest, GaussianNB

index = np.argmax([prediction, knn_prediction, random_fc_prediction, gaussian_Nbc_prediction])
classifiers = {0: 'DecisionTree', 1: 'KNN', 2: 'RandomForest', 3: 'GaussianNB'}
print('Best gender classifier is {}'.format(classifiers[index]))

print('Results...')
print("DecisionTree->", "".join(prediction))
print("KNeighbourClassifier-> ", "".join(knn_prediction))
print("RandomForestClassifier-> ", "".join(random_fc_prediction))
print("GaussianNB-> ", "".join(gaussian_Nbc_prediction))

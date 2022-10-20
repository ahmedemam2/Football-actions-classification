import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import svm

dftrain = pd.read_csv('FootballDataset.csv')
dftest = pd.read_csv('Test.csv')
y=dftrain.Label
X_train = dftrain.drop('Label',axis='columns')
y_train = dftrain.Label
X_test = dftest.drop('Label',axis='columns')
y_test = dftest.Label

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)
print(knn.predict_proba(X_test))
print(knn.predict(X_test))
print(knn.score(X_test,y_test))

X=X_train
y=y_train

clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(X, y)

print(clf.predict(X_test))


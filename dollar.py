import pandas as pd
from dollarpy import Recognizer, Template, Point

dftrain = pd.read_csv('FootballDataset.csv')
dftest = pd.read_csv('Test.csv')
y=dftrain.Label
X_train = dftrain.drop('Label',axis='columns')
X_train = X_train.drop('id',axis='columns')
y_train = dftrain.Label
X_test = dftest.drop('Label',axis='columns')
X_test = X_test.drop('id',axis='columns')


y_test = dftest.Label
print (X_train)
columns = []
for col in X_train.columns:
    columns.append(col)



templates = []
points = []
ct = 0
for index, row in X_train.iterrows():
    for i in range(0, len(columns) - 1, 2):
        points.append(Point(row[i], row[i + 1]))
    print(ct)
    ct+=1
    if ct == 4:
        templates.append(Template(y_train[index], points))
        points = []
        print(y_train[index])
        ct = 0








recognizer = Recognizer(templates)
ct = 0
points = []
for index, row in  X_test.iterrows():

    for i in range(0,len(columns)-1,2):

        points.append(Point(row[i],row[i+1]))
    ct += 1
    if ct == 4:
        result = recognizer.recognize(points)
        print(result)
        points = []
        ct = 0


















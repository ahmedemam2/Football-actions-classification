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


keys = y_train.unique()
vals = [0] * len(keys)
hash = {key: value for key, value in zip(keys, vals)}
print(hash)
templates = []
points = []
ct = 0
for index, row in X_train.iterrows():
    points = []
    for i in range(0, len(columns) - 1, 2):
        points.append(Point(row[i], row[i + 1]))


    templates.append(Template(y_train[index], points))

print (len(templates))






recognizer = Recognizer(templates)
ct = 0
points = []
for index, row in  X_test.iterrows():
    points= []
    for i in range(0,len(columns)-1,2):
        points.append(Point(row[i],row[i+1]))

    result = recognizer.recognize(points)
    if ct ==4:
        max_value = max(hash, key=hash.get)
        print(max_value)
        ct =0
        hash = {key: value for key, value in zip(keys, vals)}

    else:
        hash[result[0]]+= result[1]

    ct+=1














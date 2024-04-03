import pandas as p
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier # ensemble is the term which is used when we use multiple algorithm to predict our prediction...
import matplotlib.pyplot as plt

digit = load_digits()

# print(dir(digit))
# print('Data :',digit.data[:5])
# print('Target :',digit.target)

# plt.gray() #used to set the colormap to gray...
# for i in range(5):
#   plt.matshow(digit.images[i]) #used to represent an array as a matrix...

data = p.DataFrame(digit.data , digit.target)
data['Target'] = digit.target
# print(data.head())

x_train , x_test , y_train , y_test = train_test_split(data.drop(['Target'] , axis = 'columns') , digit.target , test_size = 0.2)
# print(len(x_train))
# print(len(x_test))

model = RandomForestClassifier()
fitting = model.fit(x_train , y_train)
prediction = model.predict(x_test)
print('The Prediction :',prediction)
score = model.score(x_test , y_test)
score_1 = model.score(x_train , y_train)
print('The Learning Accuracy of the Model :',score_1)
print('The Prediction Accuracy of the Model :',score)

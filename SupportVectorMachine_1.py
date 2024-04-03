<<<<<<< HEAD
import pandas as p
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

digit = load_digits()
# print(digit.data)
data = p.DataFrame(digit.data , columns = digit.feature_names)

data['target'] = digit.target
data['Numbers'] = data.target.apply(lambda x : digit.target_names[x])
# print(data.head())

id_variable = data.drop(['Numbers' , 'target'] , axis = 'columns')
d_variable = data.target
# print(id_variable , d_variable)

x_train , x_test , y_train , y_test = train_test_split(id_variable , d_variable , test_size = 0.2)
# print(len(x_train))
# print(len(x_test))

model = SVC()
fitting = model.fit(x_train , y_train)
prediction = model.predict(x_test)
print('The Prediction :',prediction)

score_1 = model.score(x_train ,y_train)
score_2 = model.score(x_test ,y_test)
print('The Accuracy of Model Learnig :',score_1)
=======
import pandas as p
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

digit = load_digits()
# print(digit.data)
data = p.DataFrame(digit.data , columns = digit.feature_names)

data['target'] = digit.target
data['Numbers'] = data.target.apply(lambda x : digit.target_names[x])
# print(data.head())

id_variable = data.drop(['Numbers' , 'target'] , axis = 'columns')
d_variable = data.target
# print(id_variable , d_variable)

x_train , x_test , y_train , y_test = train_test_split(id_variable , d_variable , test_size = 0.2)
# print(len(x_train))
# print(len(x_test))

model = SVC()
fitting = model.fit(x_train , y_train)
prediction = model.predict(x_test)
print('The Prediction :',prediction)

score_1 = model.score(x_train ,y_train)
score_2 = model.score(x_test ,y_test)
print('The Accuracy of Model Learnig :',score_1)
>>>>>>> 363a836121c7b865c7195e95348d4786ee1c0c56
print('The Accuracy of Model Prediction :',score_2)
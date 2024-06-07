# NavyBais Algorithm works with equation P(A/B) = P(B/A) * P(a) / P(B)

import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

data = p.read_csv(r"C:\Users\abc\Downloads\titanic.csv")
data.drop(['PassengerId' , 'Name' ,  'SibSp' , 'Parch' , 'Ticket' , 'Fare' , 'Cabin' , 'Embarked'] , axis = 'columns' , inplace= True)
# print(data.head(5))

input = data.drop('Survived' , axis = 'columns')
target = data.Survived
# print(input)
# print(target)

dummies = p.get_dummies(input.Sex)
# print(dummies)
inputs = p.concat([input , dummies] , axis = 'columns')
inputs = inputs.drop('Sex' , axis = 'columns')

print(inputs.columns[inputs.isna().any()])
# print(inputs.head(10))

inputs.Age = inputs.Age.fillna(inputs.Age.mean())
# print(inputs.head(10))

x_train , x_test , y_train , y_test = train_test_split(inputs , target , test_size = 0.3)
model = GaussianNB()
fitting = model.fit(x_train , y_train)
prediction = model.predict(x_test[:20])
print('The Prediction :',prediction)
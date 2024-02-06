import pandas as p
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import math

data = p.read_csv('/content/titanic.csv')
# print(data)

# Creating independent_variable & dependent_variable...

independent_variable = data.drop(['Survived'] , axis = 'columns')
dependent_variable = data.Survived
# print(dependent_variable)
# print(independent_variable)

# In our dataset all the fields are consist of alphabets , but we need to them into numbers...

le_PassengerId = LabelEncoder()
le_Pclass = LabelEncoder()
le_Name = LabelEncoder()
le_Sex = LabelEncoder()
le_Ticket  = LabelEncoder()
le_Cabin = LabelEncoder()
le_Embarked  = LabelEncoder()

#Joining the encoded values into the dataset...

independent_variable['PassengerId_n'] = le_PassengerId.fit_transform(independent_variable['PassengerId'])
independent_variable['Pclass_n'] = le_Pclass.fit_transform(independent_variable['Pclass'])
independent_variable['Name_n'] = le_Name.fit_transform(independent_variable['Name'])
independent_variable['Sex_n'] = le_Sex.fit_transform(independent_variable['Sex'])
independent_variable['Ticket_n'] = le_Ticket.fit_transform(independent_variable['Ticket'])
independent_variable['Cabin_n'] = le_Cabin.fit_transform(independent_variable['Cabin'])
independent_variable['Embarked_n'] = le_Embarked.fit_transform(independent_variable['Embarked'])
# print(independent_variable.head())

independent_variable_1 = independent_variable.drop(['PassengerId' , 'Pclass' , 'Name' , 'Sex' , 'Ticket' , 'Cabin' , 'Embarked'] , axis = 'columns')
# print(independent_variable_1.head(5))

#Our dataset consist of some NaN value to preprocess the data...

median_Age = math.floor(independent_variable_1.Age.median())
# print(median_Age)
independent_variable_1.Age = independent_variable_1.Age.fillna(median_Age)

                                                                # Asusuall Fitting and Predicting...
model = tree.DecisionTreeClassifier()
fitting = model.fit(independent_variable_1 , dependent_variable)
prediction = model.predict([[22.0 , 1 , 0 , 7.2500 , 0 , 2 , 108 , 1 , 523 , 147 , 2]])

if 0 in prediction:
  print('The Person may not be survived...')

elif 1 in prediction:
  print('The Person may be survived...')

score = model.score(independent_variable_1 , dependent_variable)
print('The Accuracy of the MOdel :' , score)
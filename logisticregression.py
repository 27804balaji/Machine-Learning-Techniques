<<<<<<< HEAD
import pandas as p
from matplotlib import pyplot as pl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

dataset = p.read_csv(r"C:\Users\abc\Downloads\insurance_data.csv")
# print(dataset)
plot = pl.scatter(dataset.age , dataset.bought_insurance , marker='*' , color = 'red')
print(plot)

x_train , x_test , y_train , y_test = train_test_split(dataset[['age']] , dataset.bought_insurance , test_size=0.1)
print(x_test)
model = LogisticRegression()
fitting = model.fit(x_train , y_train)
prediction = model.predict(x_test)
print(prediction)

#To predict probablity...
prediction_1 = model.predict_proba(x_test)
print(prediction_1)

if 1 in prediction:
    print('Change buy a insurance ')

elif 0 in prediction:
    print('No Change buy a insurance ')

score = model.score(x_test , y_test)
print(score)




=======
import pandas as p
from matplotlib import pyplot as pl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

dataset = p.read_csv(r"C:\Users\abc\Downloads\insurance_data.csv")
# print(dataset)
plot = pl.scatter(dataset.age , dataset.bought_insurance , marker='*' , color = 'red')
print(plot)

x_train , x_test , y_train , y_test = train_test_split(dataset[['age']] , dataset.bought_insurance , test_size=0.1)
print(x_test)
model = LogisticRegression()
fitting = model.fit(x_train , y_train)
prediction = model.predict(x_test)
print(prediction)

#To predict probablity...
prediction_1 = model.predict_proba(x_test)
print(prediction_1)

if 1 in prediction:
    print('Change buy a insurance ')

elif 0 in prediction:
    print('No Change buy a insurance ')

score = model.score(x_test , y_test)
print(score)




>>>>>>> 363a836121c7b865c7195e95348d4786ee1c0c56

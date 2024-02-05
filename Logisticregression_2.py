import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = p.read_csv(r"C:\Users\abc\Downloads\HR-Employee-Attrition1.csv")
# print(data)

dummy = p.get_dummies(data.Gender , data.MaritalStatus)
# print(dummy)
merging = p.concat([data , dummy]  , axis = 'columns')
# print(merging)
drop = merging.drop([ 'MaritalStatus' , 'Gender' , 'PerformanceRating'] , axis = 'columns')
# print(drop)

x_train , x_test , y_train , y_test = train_test_split(drop[['Age' , 'DailyRate' , 'DistanceFromHome'  ,'HourlyRate'  ,  'JobSatisfaction'  ,'MonthlyRate']] , data.PerformanceRating  , test_size = 0.3)
model = LogisticRegression()
fitting = model.fit(x_train , y_train)
prediction = model.predict(x_test)
print('The Prediction of the Performance Ratibng :' , prediction)

score = model.score(x_test , y_test)
print('The Accuracy of the Model :' , score)



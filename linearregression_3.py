import pandas as p
from sklearn.linear_model import LinearRegression

data = p.read_csv(r'c:\Users\abc\Downloads\linearregression3.csv')
# print(data)

# To print dummy columns...
dummy = p.get_dummies(data.Town)
# print(dummy)

merge = p.concat([data , dummy ], axis='columns')
# print(merge)

#We want to drop the town column from the exact dataset...

drop = merge.drop(['Town'] , axis='columns')
# print(drop)

model = LinearRegression()
# print(model)

training_x = drop.drop('Price',axis='columns')
training_y = drop.Price

#Fitting process...
fitting = model.fit(training_x , training_y)
# print(fitting)

prediction = model.predict([[7000,1,0,0]])
print('The Prediction price :',prediction)

#To find the accuracy...
score = model.score(training_x , training_y)
print('The Accuracy level of the Model :',score)


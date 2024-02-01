import pandas as p
from sklearn.linear_model import LinearRegression

dataset = p.read_csv(r'c:\Users\abc\Downloads\carprices.csv')
# print(dataset)

dummy_variable = p.get_dummies(dataset.CarModel )
# print(dummy_variable)

merging = p.concat([dataset , dummy_variable] , axis = 'columns')
# print(merging)

droping = merging.drop(['CarModel' , 'Audi A5'] , axis = 'columns' )
# print(droping)

model = LinearRegression()

training_x = droping.drop(['Price'] , axis = 'columns')
training_y = droping.Price

fitting = model.fit(training_x , training_y)
prediction = model.predict([[45000 , 4 , 1 , 0 ]])
prediction_1 = model.predict([[86000 , 7 , 1 , 0 ]])
print(f'The Prediction Price of the Mercedez Benz C class {[45000 , 4 , 1 , 0 ]} :',prediction)
print(f'The Prediction Price of the BMW X5  {[86000 , 7 , 1 , 0 ]} :',prediction_1)

score = model.score(training_x , training_y)
print('The Accuracy level of the Model is :',score)



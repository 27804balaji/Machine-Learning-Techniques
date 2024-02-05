import pandas as p
import matplotlib.pyplot as pl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = p.read_csv(r"C:\Users\abc\Downloads\archive (1)\linearregression_4.csv")
# print(dataset)
plot = pl.scatter(dataset['Mileage'] , dataset['value'])
print(plot)
plot_1 = pl.scatter(dataset['year'] , dataset['value'])
print(plot_1)

training_x = dataset[['Mileage' , 'year']]
training_y = dataset['value']

x_train , x_test , y_train , y_test = train_test_split(training_x , training_y , test_size=0.2)
model = LinearRegression()

fitting = model.fit(x_train , y_train)
prediction = model.predict(x_test)
print(prediction)

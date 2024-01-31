'''
Process of Prediction...
The Linear Regression is works on the slope and intercept concept 
The formula is y = m*x + b here
 '''

import pandas as p
import numpy as n
import matplotlib as m
import matplotlib.pyplot as pl
from sklearn import linear_model

home_price = p.read_csv(r'C:\Users\abc\Desktop\Exel\archive\home.csv')

#Setting x and y axis...
pl.xlabel('Area(sqrt feet)')
pl.ylabel('Price(INR)')
print(pl.scatter(home_price.Area , home_price.Price , color = 'red' , marker= '*') )

#Creating linear regression object...

red = linear_model.LinearRegression()
print(red.fit(home_price[['Area']] , home_price.Price)) # Inside the '[[]] ' is the Independent Variable and rest is Dependent (or) Target variable...

# Now our model is ready for the prediction...

print(red.predict(home_price[['Area']]))

# One more Test...

area = p.read_csv(r'C:\Users\abc\Desktop\Exel\archive\area1.csv')
predict = red.predict(area)

# the predicted values as a column...
area['Price'] = predict
print(area)

# Plotting in the graph...
pl.xlabel('Area(sqr feet)')
pl.ylabel('Price Prediction(INR)')
print(pl.scatter(area.Area , area.Price , color = 'blue'  , marker = '+'))
print(pl.plot(home_price.Area , predict ,color = 'black' , marker = '.' ) )

'''
red.coef_ which is consider to be as m
red.intercept_ which is consider to be as b and x the Area here...
(red.coef_* input) + red.intercept_# Which is equal to the line 22 code...
'''

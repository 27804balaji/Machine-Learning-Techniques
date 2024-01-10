import pandas as p
import numpy as n
import math
from sklearn import linear_model

home_price = p.read_csv(r'C:\Users\abc\Desktop\Exel\linearregression_2.csv')
#print(home_price)
                                                                     # Data Preprocessing...
#To remove or replace the NaN value,find median of the Bedroom...
median_bedroom = math.floor(home_price.Bedrooms.median())
#print(median_bedroom)


# Now fill the NAN values...
home_price.Bedrooms = home_price.Bedrooms.fillna(median_bedroom)
#print(home_price)

                                                                     # Model Selection...
model = linear_model.LinearRegression()

fit_1 = model.fit(home_price[['Area' ,'Bedrooms' , 'Age']] , home_price.Price)
#print(fit_1)

prediction = model.predict([[100000 , 5 , 25]])
print(f'"The Predicted price for the {[100000 , 5 , 25]}" is' , prediction)
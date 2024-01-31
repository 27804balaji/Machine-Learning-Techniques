import numpy as n

def gradient_cost(x,y):
    x_axis = y_axis = 0
    iteration = 10
    n = len(x) #because both the length of the x and y is same...
    learning_rate = 0.1

    for i in range(iteration):
        y_prediction = x_axis * x + y_axis # states that slope(y = mx + c)...
        cost = (1/n) * sum([val ** 2 for val in (y - y_prediction)])
        x_derivative = -(2/n) * sum(x * (y - y_prediction))  # derivative of x = (2/n) * sigma( x - (y - (mx + c)))
        y_derivative = -(2/n) * sum( (y - y_prediction))  # derivative of y = (2/n) * sigma((y - (mx + c))
        x_axis = x_axis - learning_rate * x_derivative 
        y_axis = y_axis - learning_rate * y_derivative 
        print('x_axis {} , y_axis {} , cost {} , iteration {} '.format(x_axis,y_axis,cost,i))
       
x = n.array([11,34,55,98,56,70])
y = n.array([34,24,67,77,91,5])
gradient_cost(x,y)           

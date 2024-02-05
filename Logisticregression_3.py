import matplotlib.pyplot as pl
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

digits = load_digits()
print(dir(digits)) # The inbuild methods in load_digits()...
print(digits.data[0]) #Using Data method...
print(digits.images[0]) #Using Images method...
print(digits.target[0:5])
pl.gray()
method_matshow = pl.matshow(digits.images[0])
print(method_matshow) #Using Images method in matplotlib...

#On the other hand...
for i in range(5):
    print(pl.matshow(digits.images[1]))

        #Let's start our program...
    
x_train , x_test , y_train , y_test = train_test_split(digits.data , digits.target , test_size=0.2)
model = LogisticRegression()

fitting = model.fit(x_train , y_train)
score = model.score(x_test , y_test)
print(digits.target[54]) #The output of this line should be equal to the next line of code if it is equal then the prediction was successfull...
prediction = model.predict([digits.data[54]])
print(prediction)
print('The Accuracy of the Model :',score)

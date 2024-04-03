<<<<<<< HEAD
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

data = pd.read_csv("C:\Users\abc\Downloads\decision.csv")
independent_variable = data.drop(['answer'], axis='columns')
dependent_variable = data.answer

# Initialize a label encoder for each categorical column
label_encoders = {}
categorical_columns = ['outlook', 'temperature', 'humidity', 'wind']

for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    independent_variable[column] = label_encoders[column].fit_transform(independent_variable[column])

# User input for prediction
outlook_1 = input('Enter the outlook: ')
temperature_1 = input('Enter the temperature: ')
humidity_1 = input('Enter the humidity: ')
wind_1 = input('Enter the wind: ')

# Transform the user input using the same label encoders
outlook_1_encoded = label_encoders['outlook'].transform([outlook_1])[0]
temperature_1_encoded = label_encoders['temperature'].transform([temperature_1])[0]
humidity_1_encoded = label_encoders['humidity'].transform([humidity_1])[0]
wind_1_encoded = label_encoders['wind'].transform([wind_1])[0]

# Train the decision tree model
model = tree.DecisionTreeClassifier()
fitting = model.fit(independent_variable, dependent_variable)

# Make a prediction
prediction_encoded = model.predict([[outlook_1_encoded, temperature_1_encoded, humidity_1_encoded, wind_1_encoded]])
print('\nWhether I can play:', prediction_encoded)

score = model.score(independent_variable, dependent_variable)
print('\nThe Learning Accuracy of the Model:', score)
print('The Prediction Accuracy of the Model:', score)
=======
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

data = pd.read_csv("C:\Users\abc\Downloads\decision.csv")
independent_variable = data.drop(['answer'], axis='columns')
dependent_variable = data.answer

# Initialize a label encoder for each categorical column
label_encoders = {}
categorical_columns = ['outlook', 'temperature', 'humidity', 'wind']

for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    independent_variable[column] = label_encoders[column].fit_transform(independent_variable[column])

# User input for prediction
outlook_1 = input('Enter the outlook: ')
temperature_1 = input('Enter the temperature: ')
humidity_1 = input('Enter the humidity: ')
wind_1 = input('Enter the wind: ')

# Transform the user input using the same label encoders
outlook_1_encoded = label_encoders['outlook'].transform([outlook_1])[0]
temperature_1_encoded = label_encoders['temperature'].transform([temperature_1])[0]
humidity_1_encoded = label_encoders['humidity'].transform([humidity_1])[0]
wind_1_encoded = label_encoders['wind'].transform([wind_1])[0]

# Train the decision tree model
model = tree.DecisionTreeClassifier()
fitting = model.fit(independent_variable, dependent_variable)

# Make a prediction
prediction_encoded = model.predict([[outlook_1_encoded, temperature_1_encoded, humidity_1_encoded, wind_1_encoded]])
print('\nWhether I can play:', prediction_encoded)

score = model.score(independent_variable, dependent_variable)
print('\nThe Learning Accuracy of the Model:', score)
print('The Prediction Accuracy of the Model:', score)
>>>>>>> 363a836121c7b865c7195e95348d4786ee1c0c56

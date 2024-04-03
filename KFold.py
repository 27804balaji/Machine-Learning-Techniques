<<<<<<< HEAD
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import numpy as n

digit = load_digits()
x_train , x_test , y_train , y_test = train_test_split(digit.data , digit.target , test_size = 0.2)
# print(len(x_train))
# print(len(x_test))

# get_score method...
  # def get_score method reads (model , x_train , x_test , y_train , y_test) as a parameter...

def get_score(model , x_train , x_test , y_train , y_test):
  model.fit(x_train , y_train)
  print(f'The Accuracy of the {model} :',model.score(x_test , y_test))


                                                              # K Fold cross validation...  
kf = KFold(n_splits = 3)
# for train_index , test_index in kf.split([1,2,3,4,5,6,7,8,9]):
#   print(train_index , test_index)

                                                              # Stratified K FoldKFold...
skf = StratifiedKFold(n_splits = 3)                                                               
x_train , x_test , y_train , y_test = train_test_split(digit.data , digit.target , test_size = 0.2)

score_of_lr = []
score_of_svc = []
score_of_rf = []
for train_index , test_index in kf.split(digit.data):
  x_train , x_test , y_train , y_test = digit.data[train_index] , digit.data[test_index] , digit.target[train_index] , digit.target[test_index]
  score_of_lr.append(get_score(LogisticRegression() , x_train , x_test , y_train , y_test))
  score_of_lr.append(get_score(SVC() , x_train , x_test , y_train , y_test))
  score_of_lr.append(get_score(RandomForestClassifier(n_estimators = 40) , x_train , x_test , y_train , y_test)) #n_estimators is used to increase the no. of trees in the RandomForestClassifier...
  

# Instead of the Above code we can use...
  # cross_val_score is a function which requires model , our x and y as the parameter...
print(cross_val_score(LogisticRegression() , digit.data , digit.target))
print(cross_val_score(SVC() , digit.data , digit.target))
=======
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import numpy as n

digit = load_digits()
x_train , x_test , y_train , y_test = train_test_split(digit.data , digit.target , test_size = 0.2)
# print(len(x_train))
# print(len(x_test))

# get_score method...
  # def get_score method reads (model , x_train , x_test , y_train , y_test) as a parameter...

def get_score(model , x_train , x_test , y_train , y_test):
  model.fit(x_train , y_train)
  print(f'The Accuracy of the {model} :',model.score(x_test , y_test))


                                                              # K Fold cross validation...  
kf = KFold(n_splits = 3)
# for train_index , test_index in kf.split([1,2,3,4,5,6,7,8,9]):
#   print(train_index , test_index)

                                                              # Stratified K FoldKFold...
skf = StratifiedKFold(n_splits = 3)                                                               
x_train , x_test , y_train , y_test = train_test_split(digit.data , digit.target , test_size = 0.2)

score_of_lr = []
score_of_svc = []
score_of_rf = []
for train_index , test_index in kf.split(digit.data):
  x_train , x_test , y_train , y_test = digit.data[train_index] , digit.data[test_index] , digit.target[train_index] , digit.target[test_index]
  score_of_lr.append(get_score(LogisticRegression() , x_train , x_test , y_train , y_test))
  score_of_lr.append(get_score(SVC() , x_train , x_test , y_train , y_test))
  score_of_lr.append(get_score(RandomForestClassifier(n_estimators = 40) , x_train , x_test , y_train , y_test)) #n_estimators is used to increase the no. of trees in the RandomForestClassifier...
  

# Instead of the Above code we can use...
  # cross_val_score is a function which requires model , our x and y as the parameter...
print(cross_val_score(LogisticRegression() , digit.data , digit.target))
print(cross_val_score(SVC() , digit.data , digit.target))
>>>>>>> 363a836121c7b865c7195e95348d4786ee1c0c56
print(cross_val_score(RandomForestClassifier(n_estimators = 40) , digit.data , digit.target))
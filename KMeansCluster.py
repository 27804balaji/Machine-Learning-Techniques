import pandas as p
import matplotlib.pyplot as pl
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

old_data = p.read_csv(r"C:\Users\abc\Downloads\income.csv" , names = [ 'Name' , 'Age' , 'Income'])
# print(old_data.drop(0))
data = old_data.drop(0)
# print(data.head())

# pl.scatter(data.Age , data.Income)
model = KMeans(n_clusters = 3) # n_clusters is used to divide the dataset into group...
fit = model.fit_predict(data[['Age' , 'Income']])
# print(fit)

data['Clusters'] = fit
# print(data)

# data_0  = data[data.Clusters == 0]
# data_1  = data[data.Clusters == 1]
# data_2  = data[data.Clusters == 2]

# pl.scatter(data_0.Age , data_0.Income  , color = 'red')
# pl.scatter(data_1.Age , data_1.Income  , color = 'grey')
# pl.scatter(data_2.Age , data_2.Income  , color = 'blue')

# pl.xlabel('Age')
# pl.ylabel('Income')
# pl.legend()

scaler = MinMaxScaler()
scaler.fit(data[['Income']])
data['Income'] = scaler.transform(data[['Income']])

scaler.fit(data[['Age']])
data['Age'] = scaler.transform(data[['Age']])
# print(data.head())

models = KMeans(n_clusters = 3)
fit = models.fit_predict(data[['Age' , 'Income']])
print(fit)

data['Cluster_1'] = fit
# print(data.head())

# print(models.cluster_centers_)
data_0  = data[data.Cluster_1 == 0]
data_1  = data[data.Cluster_1 == 1]
data_2  = data[data.Cluster_1 == 2]

pl.scatter(data_0.Age , data_0.Income  , color = 'red')
pl.scatter(data_1.Age , data_1.Income  , color = 'grey')
pl.scatter(data_2.Age , data_2.Income  , color = 'blue')
pl.scatter(models.cluster_centers_[:,0] , models.cluster_centers_[:,1] , color = 'black' , marker = '*')

pl.xlabel('Age')
pl.ylabel('Income')
pl.legend()

from sklearn.cluster import KMeans

r = range(1,23)
sse = []
for i in r:
  model_ = KMeans(n_clusters = i)
  model_.fit(data[['Age' , 'Income']])
  sse.append(model_.inertia_) # inertia_ is a method to find the sum of the square errors(sse)...

print('The Sum of the Square Error :',sse)

pl.xlabel('K')
pl.ylabel('The Sum of the Square Error ')
pl.plot(r , sse)

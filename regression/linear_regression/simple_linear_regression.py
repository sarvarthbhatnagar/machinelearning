# Simple Linear Regression

# pylot for chart plotting
import matplotlib.pyplot as plt
# pandas for file read
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')
# [columns,rows] (: = all) (-1 = all-1)
# y = dependent variable. y = f(x)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
# random_state is the seed number. it ensures common result on split for every run.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
# regressor.fit( x_train, f(x)_train)
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)


# while plotting scatter would give a scatter graph. If we use plot, that would give a linear graph on top of scatter.

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
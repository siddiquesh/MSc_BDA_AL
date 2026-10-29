# linear regression using formula
import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([2,4,5,4,5])

X_mean = np.mean(x)
Y_mean = np.mean(y)

numerator= np.sum((x - X_mean)* (y - Y_mean))
denominator = np.sum((x - X_mean) ** 2)
slope = numerator / denominator
intercept = Y_mean - slope * X_mean

print("Slope: ", slope)
print("Intercept: ", intercept)

y_pred = slope * x + intercept
print(y_pred)

plt.scatter(x,y, color="black", label="Actual Data")
plt.plot(x,y_pred, color='red', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()

# Linear Regression using pre build function
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#-1 (Rows): Tells NumPy to automatically calculate the number of rows. 
# Since there are 5 elements total, NumPy computes (5 / 1 = 5) rows.
x=np.array([1,2,3,4,5]).reshape(-1,1) 
y=np.array([2,4,5,4,5])

model=LinearRegression()
model.fit(x,y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)

y_pred=model.predict(x)

plt.scatter(x,y, color="blue", label="Actual Data")
plt.plot(x,y_pred, color='green', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import *
import pandas as pd

housing = pd.read_csv('Housing.csv')

#Select feature and Target
x= housing[["area"]]
y = housing['price']

model=LinearRegression()
model.fit(x,y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)

y_pred=model.predict(x)

print("R2 Score: ",r2_score(y,model.predict(x)))
print("MSE: ",mean_squared_error(y,model.predict(x)))

plt.scatter(x,y, color="blue", label="Actual Data")
plt.plot(x,y_pred, color='green', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()

#Select feature and Target on bedroom
x= housing[["bedrooms"]]
y = housing['price']

model=LinearRegression()
model.fit(x,y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)

y_pred=model.predict(x)

print("R2 Score: ",r2_score(y,model.predict(x)))
print("MSE: ",mean_squared_error(y,model.predict(x)))

plt.scatter(x,y, color="blue", label="Actual Data")
plt.plot(x,y_pred, color='green', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import *

x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([2,4,6,8,9])

model=LinearRegression()
model.fit(x,y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)

y_pred=model.predict(x)

print("R2 Score: ",r2_score(y,model.predict(x)))
print("MSE: ",mean_squared_error(y,model.predict(x)))

plt.scatter(x,y, color="blue", label="Actual Data")
plt.plot(x,y_pred, color='green', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()

# Load in our libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score


import os
df = pd.read_csv('Data\AmesHousing.csv')
print(df.head())

#Get number of rows and columns
print(df.shape)


# Do thuật toán hồi quy chỉ làm việc với dữ liệu dạng số nên ta chuyển các biến có kiểu categorical thành biến “Dummy”\

#Since Regression needs numerical features,convert categorical columns into dummy variables
df1= pd.get_dummies(df)
print(df1.head())

#Number of NaN values columnwise
print(df1.isna().sum())


#Define function to impute series with it's median
def impute_median(series):
    return series.fillna(series.median())
df1['Lot Frontage']= df1['Lot Frontage'].transform(impute_median)
df1['Mas Vnr Area']=df1['Mas Vnr Area'].transform(impute_median)
df1['BsmtFin SF 1']=df1['BsmtFin SF 1'].transform(impute_median)
df1['BsmtFin SF 2']=df1['BsmtFin SF 2'].transform(impute_median)
df1['Bsmt Unf SF']=df1['Bsmt Unf SF'].transform(impute_median)
df1['Total Bsmt SF']=df1['Total Bsmt SF'].transform(impute_median)
df1['Bsmt Full Bath']=df1['Bsmt Full Bath'].transform(impute_median)
df1['Bsmt Half Bath']=df1['Bsmt Half Bath'].transform(impute_median)
df1['Garage Cars']=df1['Garage Cars'].transform(impute_median)
df1['Garage Area']=df1['Garage Area'].transform(impute_median)

#Check remaining columns with NaN values
print(df1.columns[df1.isna().any()].tolist())


#Drop this column
df2=df1.drop('Garage Yr Blt',axis=1)


#Define target array y
y= df2['SalePrice'].values

#Create feature array X
X= df2.drop('SalePrice',axis=1).values

#Check X's shape
print(X.shape)

#Split the arrays into training and testing data sets
X_train, X_test,y_train, y_test= train_test_split(X,y,test_size=0.3,random_state=42)


#Create a regressor object
LR= LinearRegression()

#Fit training set to the regressor
LR.fit(X_train,y_train)

print("Mô hình hồi quy tuyến tính đã được huấn luyện, có các tham số:")
print("Intercept =", LR.intercept_)
print("Coefficients:", LR.coef_)


#Make predictions with the regressor
y_prediction = LR.predict(X_test)



# Calculate R2-score
score=r2_score(y_test,y_pred)
print('R2-score is ',score)
print('Mean_sqrd_error is==',mean_squared_error(y_test,y_prediction))
print('Root_mean_squared error of is==',np.sqrt(mean_squared_error(y_test,y_prediction)))


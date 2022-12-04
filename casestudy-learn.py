
# import  cac model hoi quy
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd 
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split


def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

#preprocessing
# tên xe(str), số cửa, chiều dài, mã lực, nguyên lieu(str), độ an toàn
def branch_name_process(df, column):
    unique_branch = list(pd.unique(df[column]))
    for idx, branch_name in enumerate(unique_branch):
        # get index
        index = df.index[df[column] == branch_name].tolist()
        df.loc[index,column] = int(idx)
    return df

# Quy trinh xay dung mo hinh  hoi quy tuyen tinh
# b1: chon feature dac trung nao de dua mo hinh du doan
df = pd.read_csv("data\Case_study_CarPrice_Assignment.csv")
df['BranchName'] = df.apply(lambda x:str(x['CarName']).split(" ")[0],axis=1).reset_index(drop=True)

# su dung cong cu cua pandas(requirments: du  lieu cot nay phai co dinh, ko thay doi)
df['BranchName'] = df['BranchName'].astype('category').cat.codes
# tmp = df.corr()

# print(tmp.head(1))

# b2: loc nhieu(cuc ky quan trong)
target = df[['carwidth','curbweight','enginesize','citympg','highwaympg','BranchName', 'price']]
# print(target.head(5))
# carwidth,curbweight,enginesize,citympg,highwaympg,BranchName, price
# boxplot , 6-7 sort theo values


# b3: normalizer data 

# b4: chon mo hinh (overview, compare cac mo hinh lai vs nhau: metrics)

# linear, randomforest, bootrap
# poly = PolynomialFeatures(degree=2, include_bias=False)


# split du lieu
X, y = target[['carwidth','curbweight','enginesize','citympg','highwaympg','BranchName']], df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)

pred = regressor.predict(X_test)
print("MAPE: ",mean_absolute_percentage_error(y_test, pred))
# metrics
# Hyper parameters range intialization for tuning 
from sklearn.model_selection import GridSearchCV
parameters={"splitter":["best","random"],
            "max_depth" : [1,3,5,7,9,11,12],
           "min_samples_leaf":[1,2,3,4,5,6,7,8,9,10],
           "min_weight_fraction_leaf":[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],
           "max_features":["auto","log2","sqrt",None],
           "max_leaf_nodes":[None,10,20,30,40,50,60,70,80,90] }

tuning_model=GridSearchCV(regressor,param_grid=parameters,scoring='neg_mean_squared_error',cv=3,verbose=3)
tuning_model.fit(X_train, y_train)
y_pred =tuning_model.best_estimator_.predict(X_test)
print("MAPE: ",mean_absolute_percentage_error(y_test, pred))

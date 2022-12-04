import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

df = pd.read_csv("Data\Credit_Scoring.csv")
print(df.head())


# thông tin dữ liệu
print(df.info())


# mô tả dữ liệu
print(df.describe())


# kiểm tra dữ liệu khuyết thiếu
print(df.isna())

# loại bỏ dữ liệu khuyết thiếu
df1 = df.dropna()


# % số lượng bản ghi còn lại
print(100 * df1.shape[0]/df.shape[0])

# vẽ biểu đồ phân bố
sns.kdeplot(df1["MonthlyIncome"])


# thay thế dữ liệu khuyết thiếu bởi giá trị nội suy theo cột
df2 = df.interpolate(axis=1) 


# vẽ biểu đồ boxplot cho các đặc trưng
df2.boxplot()


# vẽ biểu đồ box plot cho MonthlyIncome
sns.boxplot(df2["MonthlyIncome"])


# lọc dữ liệu ngoại lai
df3 = df2[~((df2 < (Q1 - 1.5 * IQR)) | (df2 > (Q3 + 1.5 * IQR))).any(axis=1)]



df3.boxplot()



sns.boxplot(df3["MonthlyIncome"])


# phân bố dữ liệu trên cột MonthlyIncome
sns.kdeplot(data = df3['MonthlyIncome'])


# chuẩn hóa với minmax scaling
scaler = MinMaxScaler()


mms = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))


sns.kdeplot(data = mms)


# chuẩn hóa với robust scaling
scaler = RobustScaler()

rbs = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))


sns.kdeplot(data = rbs)


# chuẩn hóa với standard scaling
scaler = StandardScaler()

sc = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))
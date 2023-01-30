#XÂY DỰNG MÔ HÌNH DỰ BÁO GIÁ NHÀ/M2 DỰA TRÊN BÀI TOÁN MUA BÁN ĐẤT CỦA HUYỆN THẠCH THẤT
import pandas as pd
import numpy as np
from numpy import nan
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
from sklearn.metrics import r2_score


def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


df=pd.read_csv('Data\LandTrading.csv')
# Mô tả dữ liệu
# print(df.shape)

# Trích xuất các bản ghi của huyện Thạch Thất.
df1=df[df['ten_quan']=='Huyện Thạch Thất'].reset_index()
print(df1.head())

# Thống kê mô tả dữ liệu
print(df1.dtypes)
print(df1.describe())


# # Kiểm tra nếu có tồn tại dữ liệu null
print(df1.isnull().values.any())
print(df1.isnull().sum())


# Trực quan dữ liệu khuyết thiếu
# plt.figure(figsize = (4,4)) #is to create a figure object with a given size
# sns.heatmap(df1.isna(), yticklabels=False, cbar=False)
# plt.show()

feature_selected=['dien_tich', 'so_do', 'mat_tien', 'gia_m2','lat','long','ten_duong','huong_nha']
df1=df1[feature_selected]

# XỬ LÝ DỮ LIỆU CỘT DIỆN TÍCH
sns.boxplot(df1['dien_tich'])
plt.title('du lieu mat tien truoc xu ly ngoai lai')
plt.show()

# xử lý dữ liệu ngoại lai
Q1 = df1['dien_tich'].quantile(0.25)
Q3 = df1['dien_tich'].quantile(0.75)
IQR = Q3 - Q1

df1 = df1[~((df1['dien_tich'] < (Q1- 1.5 * IQR) ) | (df1['dien_tich'] > (Q3 + 1.5*IQR)))]
print(df1.head())
sns.boxplot(df1['dien_tich'])
plt.title('du lieu mat tien sau xu ly ngoai lai')
plt.show()

# dien gia tri khuyet thieu
df1['dien_tich'].fillna(df1['dien_tich'].median(), inplace=True)
print(df1.head(10))
print('tổng số bản ghi sau khi loại bỏ ngoại lai diện tích')
print(df1.info())

## XỬ LÝ DỮ LIỆU CỘT MẶT TIỀN
sns.boxplot(df1['mat_tien'])
plt.title('du lieu mat tien truoc xu ly gia tri ngoai lai')
plt.show()

# xử lý dữ liệu ngoại lai
Q1 = df1['mat_tien'].quantile(0.25)
Q3 = df1['mat_tien'].quantile(0.75)
IQR = Q3 - Q1


df1 = df1[~((df1['mat_tien'] < (Q1- 1.5 * IQR) ) | (df1['mat_tien'] > (Q3 + 1.5*IQR)))]
print(df1.head())
sns.boxplot(df1['mat_tien'])
plt.title('du lieu mat tien sau xu ly gia tri ngoai lai')
plt.show()

# điền giá trị khuyết thiếu
df1['mat_tien'].fillna(df1['mat_tien'].median(), inplace=True)
print(df1['mat_tien'].head(10))
print('tổng số bản ghi sau khi loại bỏ ngoại lai mặt tiền')
print(df1.info())



## XỬ LÝ DỮ LIỆU CỘT GIÁ_m2
sns.boxplot(df1['gia_m2'])
plt.title('du lieu gia_m2 truoc xu ly gia tri ngoai lai')
plt.show()

# xử lý dữ liệu ngoại lai
Q1 = df1['gia_m2'].quantile(0.25)
Q3 = df1['gia_m2'].quantile(0.75)
IQR = Q3 - Q1


df1 = df1[~((df1['gia_m2'] < (Q1- 1.5 * IQR) ) | (df1['gia_m2'] > (Q3 + 1.5*IQR)))]
print(df1.head())
sns.boxplot(df1['gia_m2'])
plt.title('du lieu giá_m2 sau xu ly gia tri ngoai lai')
plt.show()

# điền giá trị khuyết thiếu
df1['gia_m2'].fillna(df1['gia_m2'].median(), inplace=True)
print(df1['gia_m2'].head(10))
print('sau khi loại bỏ ngoại lai - gia/m2')
print(df1.info())



## XỬ LÝ DỮ LIỆU LAT, LONG
# điền giá trị khuyết thiếu
df1["lat"].fillna(df1["lat"].mode()[0],inplace=True)
df1["long"].fillna(df1["long"].mode()[0],inplace=True)
print(df1.info())


# # XỬ LÝ DỮ LIỆU HƯỚNG NHÀ
print(df1['huong_nha'].unique())
print(df1['huong_nha'].value_counts())
df1['huong_nha']= df1['huong_nha'].str.replace('-', ' ')
print(df1['huong_nha'].value_counts())
df1['huong_nha']=df1['huong_nha'].fillna('unknown').astype('category').cat.codes
print(df1['huong_nha'].unique())



# XỬ LÝ DỮ LIỆU SỔ ĐỎ
# # # # TIỀN XỬ LÝ CỘT SO_DO:
# # print(df1['so_do'].unique())
def convert_landcert(certificate):
    try:
        certificate = certificate.lower()
        if _found_text(certificate, ['sổ đỏ', 'sổ hồng', 'có sổ', 'sẵn sổ', 'sđcc', 'miễn phí sang tên', 'sổ mới','công chứng']):
            return '1'
        else:
            return '0'
    except:
            return None
        
def _found_text(text, list_item):
    # check whether the text contains any item within the list_item
    for item in list_item:
        if item in text:
            return True
    return False    

df1['so_do_test']= df1.apply(lambda x: convert_landcert(x['so_do']),axis=1)
print(df1.head())
print(df1['so_do_test'].value_counts())
df1['so_do_test']=df1['so_do_test'].fillna('unknown').astype('category').cat.codes
print(df1.info())


# # XỬ LÝ DỮ LIỆU TÊN ĐƯỜNG
# # print(df1['ten_duong'].unique())
def convert_roadname(name):  ## 
    try:
        name = name.lower()
        if _found_text(name, ['419']):
            return 'đường tỉnh lộ 419'
        elif _found_text(name, ['21']):
            return 'đường tỉnh lộ 21'
        elif _found_text(name, ['21A']):
            return 'đường tỉnh lộ 21A'
        elif _found_text(name, ['21B']):
            return 'đường tỉnh lộ 21B'
        elif _found_text(name, ['446']):
            return 'đường quốc lộ 446'
        elif _found_text(name, ['84']):
            return 'đường tỉnh lộ 84'
        elif _found_text(name, ['420']):
            return 'đường tỉnh lộ 420'
        else:
            return name
    except:
            return None
        
def _found_text(text, list_item):
    # check whether the text contains any item within the list_item
    for item in list_item:
        if item in text:
            return True
    return False    

df1['ten_duong_test']= df1.apply(lambda x: convert_roadname(x['ten_duong']),axis=1)
print(df1.head(30))
print(df1.info())

df1['ten_duong_test']=df1['ten_duong_test'].fillna('unknown').astype('category').cat.codes
print(df1['ten_duong_test'].unique())


#Chuẩn hóa với StandardScaler
df1=df1.drop(columns=['so_do','ten_duong'])
print(df1.info())
X = df1.drop(columns=['gia_m2'], axis=1)
y = df1[['gia_m2']]
print(X.columns.tolist())

scaler = StandardScaler()
df_scaler = scaler.fit_transform(X)
X=X.values
y=y.values

print(X,y)

y= y.reshape(-1,1)
print(X.shape)
print(y.shape)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print("start training")
reg = LinearRegression().fit(X_train, y_train)
# mape :
y_pred = reg.predict(X_test)
print("mape", mean_absolute_error(y_test, y_pred))


# đánh giá mô hình
y_pred = reg.predict(X_test) 
## tính toán R2 của model
r2_train = r2_score(y_train, reg.predict(X_train))
print("R2 trên tập huấn luyện của model là:" + str(r2_train))
r2_test = r2_score(y_test, y_pred)
print("R2 trên tập kiểm tra của model là:" + str(r2_test))
print('Sai số dự báo trung bình:', metrics.mean_absolute_error(y_test, y_pred))  


# Infer Model
#   dien_tich              mat_tien         lat        long      huong_nha  so_do_test  ten_duong_test
# huong_nha: 0:9
#ten_duong_test: 0:16
input = [120, 6,21.0,105.5,8,2,0 ]
input = np.array(input).reshape(1,-1)
infer_test = reg.predict(input)
print(infer_test)
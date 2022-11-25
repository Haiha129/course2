import pandas as pd
df=pd.read_csv('Data\shopeep_koreantop_clothing_shop_data.csv')


# Để đơn giản ta thực hiện lọc tập dữ liệu ban đầu theo các thuộc tính sau
df = df[['date_collected','shop_location','response_time']]
print(df)

# Tách cột dữ liệu có kiểu chuỗiTa có thể sử dụng các phép toán tách chuỗi splitHàm str.split(‘Ký tự phân cách’) 
# có tác dụng tách chuỗi ban đầu str thành các chuỗi con được ngăn cách nhau bởi ký tự phân cách

# Tách cột shop_location thành 2 cột District và City
df['District']=df['shop_location'].str.split(',').str[0]
df['City']=df['shop_location'].str.split(',').str[1]
print(df)

# TO_DATETIME (This function converts a scalar, array-like, Series or DataFrame/dict-like to a pandas datetime object.)
#  Series.dt.year: The year of the datetime.

# Tách cột date_collected thành 3 cột Day, Month, Year #SỬ DỤNG pd.to_datetime
df['Day']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.day
df['Month']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.month
df['Year']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.year
print(df)


df['test']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d')
print(df['test'])

#Tách cột dữ liệu có kiểu thời gian
# Tách cột response_time thành 3 cột Hour, Minute, Second
df['Hour']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.hour
df['Minute']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.minute
df['Second']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.second
print(df)
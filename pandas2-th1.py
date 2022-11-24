import pandas as pd
df=pd.read_csv('Data\FoodPrice_in_Turkey.csv')
# print(df.info())

#Xóa các dòng có thuộc tính ProductID trùng nhau, giữ lại bản ghi cuối cùng, giữ chỉ số ban đầu của các dòng

# df=df.drop_duplicates(['ProductId'],keep='last')
# print(df.head())

# Xóa các dòng có thuộc tính ProductID trùng nhau, giữ lại bản ghi cuối cùng, thiết lập lại chỉ số
df=df.drop_duplicates(['ProductId'],keep='last').reset_index(drop=True)
print(df.head())

# Tách file chứa thông tin sản phẩm
df_info=df.loc[:,['Place','ProductId','ProductName','UmId','UmName']]
print(df_info.info())

# Tách file chứa thông tin giá
df_info=df.loc[:,['ProductId','ProductName','Price']]
print(df_info.info())

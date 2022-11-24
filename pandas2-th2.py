import pandas as pd
df=pd.read_csv('Data\FoodPrice_in_Turkey.csv')
# print(df.head())

# Tách file 1 chứa 5000 bản ghi đầu tiên
df_extract1 = df.loc[0:4999,:]
# print(df_extract1.info())

# Tách file 2 chứa các bản ghi còn lại
# df_extract2 = df.loc[5000:7380,:]
# print(df_extract2.info())
# print(df_extract2.tail(1))

# Tách file 3 chứa thông tin giá với số dòng từ bản ghi 1000 đến 2000
# df_extract3 = df.loc[1000:2000,"Price"]
# print(df_extract3.head(2))


#CONCAT: When objs contains at least one DataFrame, a DataFrame is returned; if not, a Series is returned.
#GHÉP CÁC DÒNG
# new_df_1=pd.concat([df_extract1,df_extract2])
# print(new_df_1.head())

# df_extract_column1=df.loc[0:10,['Place','ProductId']]
# # print(df_extract_column1.info())
# df_extract_column2=df.loc[0:10,['Price']]
# # print(df_extract_column2.info())
# new_df_column12=pd.concat([df_extract_column1,df_extract_column2])
# print(new_df_column12)
# print(type(new_df_column12))
# new_df_column123=pd.concat([df_extract_column1,df_extract_column2],axis=1)
# print(new_df_column123)
# print(type(new_df_column123))

# Concat -- names?
# new_df_test1=pd.concat([df_extract_column1,df_extract_column2], keys = ['df_extract_column1', 
# 'df_extract_column2'], names=['so 1', 'so 2'])
# print(new_df_test1)

# #concat --- join
df_1=df.loc[0:10,['Place','ProductId','ProductName']]
df_2 = pd.DataFrame([[2, 3], [4, 5]], columns=list('PQ'))
# df_combine12=pd.concat([df_1, df_2],join='inner', axis=1)
# print(df_combine12)
df_combine121=pd.concat([df_1, df_2],axis=1)
print(df_combine121)


#APPEND

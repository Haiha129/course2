import pandas as pd

# Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
df=pd.read_csv('Data\GDPlist.csv', encoding= 'unicode_escape')
# print(df.info())
# # Tính giá trị lớn nhất và nhỏ nhất của GDP.
# print(df['GDP (millions of US$)'].min())
# print(df['GDP (millions of US$)'].max())

# Hãy cho biết xu hướng phân bố dữ liệu của GDP.

# Hãy cho biết châu lục nào xuất hiện nhiều nhất?
# print(df.Continent.value_counts()) #nếu tên cột có khoảng trắng -->df['ten cot'].value_counts()

# Với mỗi châu lục hãy tính tổng GDP; trung bình cộng GDP.
# df.groupby('Continent').agg(['sum', 'mean']))
df_sum=df.groupby('Continent').sum()
df_mean=df.groupby('Continent').mean()
# print(df_sum)
# print(df_mean)
#  Hợp nhất 2 bảng này thành một bảng duy nhất gồm 3 thông tin: Tên châu lục; Tổng GDP; TBC GDP.
# SYNTAX: pandas.concat(objs, *, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True)
print('*'*50)
df_merge=pd.concat([df_sum, df_mean],keys=['Tổng GDP', 'TBC GDP'], axis=1)
print(df_merge)
import pandas as pd
df=pd.read_csv('Data\OnlineRetail.csv')
# print(df.info())

# Hãy giải đáp các thắc mắc sau:Công ty bán hàng do bao nhiêu nước sản xuất
# SYNTAX: series.unique() --> return unique values from series object.
df_country = df.Country.unique() #--> return a numpy.ndarray
#SYNTAX: numpy.ndarray.size --> number of elements in array
# print(df_country.size)


# Tổng số lượng đơn hàng bán ra, tổng doanh thu
print('TỔNG SỐ LƯỢNG ĐƠN HÀNG BÁN RA:')
df_count1=df.InvoiceNo.unique()
print(df_count1.size) #????

print('TỔNG DOANH THU BÁN RA:')
df['Total']=df['Quantity']*df['UnitPrice']
print(df['Total'].agg(sum))

# Top 10 mặt hàng có số lượng bán ra lớn nhất #BẢNG DỮ LIỆU NÀY TỒN TẠI GIÁ TRỊ ÂM
df_bestsell=df.groupby(['StockCode', 'Description'])['Quantity'].agg(sum).sort_values(ascending=False)
print(df_bestsell.head())
# Top 10 mặt hàng có doanh thu lớn nhất
df_toprevenue=df.groupby(['StockCode','Description'])['Total'].agg(sum).sort_values(ascending = False)
print(df_toprevenue.head())
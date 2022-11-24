#Cú pháp của Pivot table gồm:
#pandas.pivot_table(values=’a’, index=’b’, columns=’c’, aggfunc='mean’)
#Kết quả tạo ra một bảng trong đó các giá trị của thuộc tính b nằm trên các hàng, 
#các giá trị của thuộc tính c nằm trên các cột 
#các ô giao nhau là các giá trị của a được tính theo các hàm trong aggfunc (các ô nhận giá trị NaN nếu dữ liệu bị thiếu).

import pandas as pd
df = pd.read_csv('Data\OnlineRetail.csv')
#Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
# print(df.info())

# Xây dựng bảng Pivot table, với mỗi Số hóa đơn tính trung bình cộng số lượng các mặt hàng theo từng Quốc gia.
print("-"*50)
df_tbc=df.pivot_table(index = 'InvoiceNo', columns =['StockCode','Country'], values = 'Quantity', aggfunc = 'mean') 
# print(df_tbc.head())
# Xây dựng bảng Pivot table, với mỗi Khách hàng cho biết số lượng mua hàng lớn nhất và nhỏ nhất theo Kho.
# df_mm=df.pivot_table(index='StockCode', columns ='')
df_max=df.pivot_table(index = 'customer id', columns =['StockCode'], values = 'Quantity', aggfunc = 'max') 
print(df_max.head())
# Xây dựng bảng Pivot table, với mỗi Mã kho tính tổng số lượng các mặt hàng và trung bình cộng giá.
# Xây dựng bảng Pivot table cho biết tổng số lượng hàng bán được của mỗi ngày.
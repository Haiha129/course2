# Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
import pandas as pd
df=pd.read_csv('Data\OnlineRetail.csv')
# print(df.info())
# Trích xuất dữ liệu các cột Description và Quantity lưu vào file OnlineRetail.csv
df_extract1=df.loc[:,['Description', 'Quantity']]
df_extract1.to_csv('OnlineRetail_extract1.csv')

# # Trích xuất dữ liệu 1000 dòng đầu tiên lưu vào file OnlineRetail.xlsx
df_extract2=df.loc[0:1000]
df_extract2.to_excel('OnlineRetail_extract2.xlsx')

# Trích xuất các bản ghi có số lượng từ 10 trở lên lưu vào file OnlineRetail.h5
df_extract3=df[df['Quantity']>10]
print(df.to_hdf('OnlineRetail.h5',key='df', mode='w'))
df_extract3.to_hdf('OnlineRetail.h5','table')
# Trích xuất dữ liệu các phần tử từ dòng 1000 đến dòng 2000, các cột Quantity, InvoiceDate, UnitPrice lưu vào file OnlineRetail.json
df_extract4 = df.loc[1000:2000,'Quantity':'UnitPrice']
df_extract4.to_json('OnlineRetail.json')
# Trích xuất các bản ghi có số hóa đơn ‘536365’ lưu vào file OnlineRetail.html
df_extract5 =df.iloc[:,'InvoiceNo'==536365]
print(df_extract5.head())
import pandas as pd
df=pd.read_csv('Data\FoodPrice_in_Turkey.csv')


#ĐỔI TÊN CỘT
df.rename(columns={'Place':'Địa điểm','ProductName':'Tên SP'},inplace=True)
print(df.head())

# THÊM CỘT MỚI GIÁ TRỊ RỖNG
df['new_column'] = 'NaN'
print(df.head())

# Thêm cột giảm giá 10% cho tất cả các bản ghi
# Cách 1: Gán tên cột dưới dạng một chuỗi và thêm giá trị cho cột đó

df['Giảm giá 1']= pd.Series('10%', index=df.index)
print(df.head())
# Cách 2: Sử dụng phương thức insert() gồm 3 đối số
# - đối số đầu tiên là chỉ mục (vị trí) muốn chèn cột mới (chỉ mục là 10--> cột mới được thêm vào vị trí 11 của DataFrame)
# - đối số thứ hai là tên của cột mới muốn chèn 
# - đối số thứ ba giá trị của cột

df.insert(10,'Giảm giá 2',pd.Series('12%', index=df.index))
print(df.head())


#THÊM DÒNG
# Sử dụng phương thức append() thêm một dòng vào cuối DataFrame

df=df.append({'Địa điểm':'NA','ProductId':'RR','Tên SP':'Rice','UmId':10,'UmName':'KG','Month':6,'Year':2021,'Price':84.3785,'Giảm giá':'10%','Giảm giá 2':'12%'},ignore_index=True)
print(df.tail())  # Hiển thị 5 bản ghi cuối


#XÓA CỘT SỬ DỤNG DROP - ngoài ra có del, pop
# Cú pháp: df.drop('column_name', axis=1, inplace=True)
# Trong đó axis = 1 là xóa cột; inplace = True xóa trục tiếp trên dữ liệu gốc mà không phải tạo bản sao

df.drop('Giảm giá 1', axis=1, inplace=True)
print(df)
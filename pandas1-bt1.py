#Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
import pandas as pd
df=pd.read_csv('Data\GDPlist.csv', encoding='cp1252')
print(df.info())

#Việt hóa tên các cột trong bảng dữ liệu: Country 🡪 Nuoc; Continent 🡪 Chauluc; GDP (millions of US$) 🡪 GDP (trieu $)
df.rename(columns={'Country': 'Nuoc', 'Continent': 'Chau luc', 'GDP (millions of US$)': 'GDP(trieu $)'}, inplace=True)
print(df.head())

# #Chèn thêm một cột “Thanhpho” vào sau cột “Nuoc”, giá trị ban đầu là giá trị của cột “Nuoc” 
df.insert(1, 'Thanh pho',pd.Series(df['Nuoc'])) #Cách 1
# df.insert(1, 'Thanh pho', df.loc[:,'Nuoc'] #Cách 2
print(df.head())

#Trong cột Thanhpho, thay giá trị Vietnam thành Hanoi; Làm tương tự với các nước còn lại.
# df.at[1,'Thanh pho']="Af123"

# print(df.head())
# print(df)
# Xóa các bản ghi có Chauluc là ‘Asia’
df_filter1=df[df['Chau luc']=='Asia'].index
df.drop(df_filter1, inplace=True)
print(df.head())

# Xóa các bản ghi có GDP < 300000
df_filter1=df[df['GDP(trieu $)']<300000].index
df.drop(df_filter1, inplace=True)
print(df.head())

import pandas as pd
# Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
df=pd.read_excel('Data\house_price_dống-da.xlsx')
# print(df.info())

# Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên
print(df[['type_of_land','ward_name']])

# Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên.
# bedroom>=3
# land_certificate=='Sổ đỏ'
print(df[(df['bedroom']>=3)&(df['land_certificate']=='Sổ đỏ')][['address','price','house_direction','balcony_direction']])


# Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất.
df_group1=df.groupby(['type_of_land'])['price'].agg(['mean','max','min'])
print(df_group1)
# Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường.
df_group2=df.groupby('ward_name')[['bedroom','toilet','floor']].agg('mean')
print(df_group2)
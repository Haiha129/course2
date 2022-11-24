# Đọc dữ liệu vào DataFrame

import pandas as pd
df=pd.read_csv('Data\FoodPrice_in_Turkey.csv', sep = ',')
print(df.head())

# ghi dữ liệu từ dataframe vào file csv
df.to_csv('democsv_FoodPrice.csv')

# ghi dữ liệu từ dataframe vào file excel
df.to_excel('demoexcel_Food.xlsx')

#Ghi dữ liệu từ DataFrame vào file Json
df.to_json('demojson_FoodPrice.json',orient='columns') 

# Tham số orient được sử dụng để xác định định dạng dữ liệu đầu ra, có thể là:
# Các bản ghi – records
# Các cột – columns
# Các chỉ mục – indexs
# Các giá trị – values
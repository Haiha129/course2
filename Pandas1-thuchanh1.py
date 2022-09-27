import pandas as pd

# đọc file csv
df = pd.read_csv("Data\FoodPrice_in_Turkey.csv")
print(df.head())

# đọc file excel
df = pd.read_excel('Data\house_price_dống-da.xlsx')
print(df.head())

# chuyển file từ csv sang json
df = pd.read_csv('Data\FoodPrice_in_Turkey.csv')
df.to_json('Data\FoodPrice_in_Turkey.json')
df = pd.read_json('Data\FoodPrice_in_Turkey.json')
print(df.info())


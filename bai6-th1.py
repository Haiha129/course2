import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Data\FoodPrice_in_Turkey.csv')
data1 = df[(df['Year'] == 2019) & (df['Month'] == 12) & (df['ProductName'] == 'Rice - Retail')]
plt.bar(data1['Place'], data1['Price'])
plt.show()


# Tinh chỉnh thuộc tính biểu đồ

plt.bar(data1['Place'], data1['Price'], width = 0.5)
plt.title('Rice Price in 12/2019', fontsize = 16, color = 'r')
plt.xlabel('Place', fontsize = 14)
plt.ylabel('Price', fontsize = 14)
plt.show()


data2 = df[(df['Place'] == 'National Average') & (df['Year'] == 2019) & (df['ProductName'] == 'Rice - Retail')]
plt.plot(data2['Month'], data2['Price'])
plt.show()

plt.plot(data2['Month'], data2['Price'], linewidth = 2, marker = '*', markersize=10, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.title('Rice Price of National Average in 2019', fontsize = 16, color = 'r')
plt.xlabel('Month', fontsize = 14)
plt.ylabel('Price', fontsize = 14)
plt.show()


x = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Year'] == 2019)]
y = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Rice - Retail') & (df['Year'] == 2019)]

plt.scatter(x['Price'], y['Price'])
plt.show()



plt.scatter(x['Price'], y['Price'], s = 50)
plt.title('Relationship between Rice Price and Gas Price', fontsize = 16, color = 'r')
plt.xlabel('Gas', fontsize = 14)
plt.ylabel('Rice', fontsize = 14)
plt.show()
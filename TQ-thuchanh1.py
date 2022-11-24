import pandas as pd
df=pd.read_csv('Data\subset-covid-data.csv')
#DISPLAY ALL COLUMNS AND ROWS
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df.info())

#Liệu các quốc gia có số lượng ca mắc mới trong ngày 12-4-2020 giống nhau hay không
print(df.date.value_counts()) #object containing unique values
cleaned_data = df[df.date == '2020-04-12'] #lọc dữ liệu

# Vẽ biểu đồ phân bố số lượng ca mắc mới ở các quốc gia
print ("trung bình số ca mắc mới: " + str(cleaned_data.cases.mean()))
print ("trung vị của số ca mắc mới: "+ str(cleaned_data.cases.median()))
import matplotlib.pyplot as plt
plt.hist(cleaned_data.cases, bins = 200)
plt.title("Phân bố số ca mắc mới")
plt.xlabel("số số ca mắc mới")
plt.ylabel("Số lượng quốc gia")
plt.show()


#Tổng số lượng người mắc bệnh của từng châu lục, tử vong--> group châu lục, ca mắc --> tính tổng
print('Tổng số lượng người mắc mới, tử vong của từng châu lục:  ')
df_group = df.groupby('continent')['cases', 'deaths'].agg(sum) # cách thể hiện khác?
print(df_group.head())

#Top 5 quốc gia có số lượng ca mắc mới lớn nhất, tử vong lớn nhất.
#SYNTAX: DataFrame.sort_values(self, by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

# print('Các quốc gia có số lượng ca tử vong lớn nhất: ')
print(df.sort_values(by='cases', ascending = False).head())

# print('Top 5 quốc gia có lượng người tử vong lớn nhất: ')
print(df.sort_values(by='deaths', ascending = False).head())



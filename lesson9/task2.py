# Задача 59. Выполнить для файлов из лекции:
# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000

import pandas as pandas
df = pandas.read_csv('lesson9\sample_data\california_housing_test.csv')
print('============') 

print(df.isnull().sum())
print() # или
print(df.isna().sum())
print('------------') 

print(df[df['median_income'] < 2].median_house_value.mean())
print() # или 
print(df[df.median_income < 2].median_house_value.mean())
print('------------') 

print(df[['longitude', 'latitude']])
print() # или 
print(df.iloc[:,[0, 1]])
# или "срез"
# print(df.iloc[:,:2])
# или
# print(df[df.columns[:2]])
print('------------') 


print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])
print('============')


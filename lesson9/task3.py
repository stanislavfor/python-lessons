# Задача 3.  Выполнить для файлов из лекции:
# 1. Определить какое максимальное и минимальное значение median_house_value
# 2. Показать максимальное median_house_value, где median_income = 3.1250
# 3. Узнать какая максимальная population в зоне минимального значения median_house_value

import pandas as pandas
df = pandas.read_csv('lesson9\sample_data\california_housing_test.csv')

min_max_value = df['median_house_value'].min(), df['median_house_value'].max() 
print(min_max_value)

max_median_house_value = df[df.median_income == 3.1250] ['median_house_value'].max()
print(max_median_house_value)

min_median_house_value = df[df.median_house_value == df['median_house_value'].min()] ['population'].max()
print(min_median_house_value)
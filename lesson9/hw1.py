# Задача 1. Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd
df = pd.read_csv('..\california_housing_train.csv')

print(df['population'].min())
# 3.0

print(df[df['population'] < 500].median_house_value.mean())
# 206683.83635227982


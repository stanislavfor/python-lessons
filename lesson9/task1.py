# Задача 57. Выполнить для файлов из лекции:
# 1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
# 2. Посмотреть сколько в нем строк и столбцов.
# 3. Определить какой тип данных имеют столбцы.

# Подключение GoogleДиск:
# from google.colab import drive
# drive.mount('/content/gdrive', force_remount=True)

import pandas as pandas
df = pandas.read_csv('lesson9\sample_data\california_housing_test.csv')

print(df.head())

print(df.sample(5))

print(df.shape)

print(df.dtypes)

print(df.info())



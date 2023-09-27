# Задача 63. Выполнить для файлов из лекции:
# Ресурс [colab.research.google.com](https://colab.research.google.com/)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# from google.colab import drive
# drive.mount('/content/gdrive')

# 1. Изобразите отношение households к population с помощью точечного графика

df = pd.read_csv('lesson10/sample_data/california_housing_train.csv')
print(df)
df.sample(5)
sns.scatterplot(data=df, x='households', y='population')

# --------------------------------
# csv 
# #- comma-separated values - данные разделенные запятой
# df = pd.read_csv('file.csv', # функция считывания внешнего файла формата csv (можно выбрать необходимый формат)
                #  encoding='windows-1251',
                #  headler=0,  # - какую строку считать заголовком(по умолчанию нулевую)
                #  sep = ';',
                #  index_col='название_столбца',
                #  parse_dates=['Date'],
                #  dayfirst=True)
# 'file.csv' - путь к файлу,
# sep - разделитель sep(по умолчаниию ',')
# encoding – параметр в read_csv, отвечает за кодировку текста, которая может быть различной. Самая распространённая – utf
# index_col='название_столбца' - название столбца, который будет выступать как столбец индексов
# index_col=[0] - индекс столбца, который будет выступать как столбец индексов
# parse_dates – указывает, стоит ли воспринимать даты как даты (по умолчанию они воспринимаются пандасом как строки).
    # пример pd.read_csv(path, parse_dates=['some_date', 'another_date'])
    # Параметр с датами может принимать несколько значений:
    # True – пытается перевести в дату первую колонку
    # список колонок – parse_dates=['some_date', 'another_date']
    # пытается перевести в дату указанные в списке колонки и столбцы create_data, payment_data
    # будут обрабатываться как даты
# dayfirst=True  - первое значение в дате это день или нет - True/False
# df['Date'].dt.day - номер дня недели в соответствии с данными в колонке с датами !!!!!
# df['Date'].dt.day_name() - название дня недели в соответствии с данными в колонке с датами
# df['Date'].dt.month - номер месяца в соответствии с данными в колонке с датами
# df['Date'].dt.month_name() - название месяца в соответствии с данными в колонке с датами
# --------------------------------

sns.set(rc={'figure.figsize':(11.7,8.27)})

# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график

sns.relplot(x='longitude', y='median_house_value', kind='line', data=df)
sns.relplot(x=df.longitude, y=df.median_house_value, kind='line')

# 3. Представить гистограмму по housing_median_age

sns.histplot(data=df, x='housing_median_age')



# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age

plt.figure(figsize=(16, 10))
sns.histplot(df, x='median_house_value', hue='housing_median_age')
plt.xticks(range(0, 550000, 25000), rotation=45)
plt.yticks(range(0, 26, 1));
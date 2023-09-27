# Задача 65. Написать EDA для датасета про пингвинов. Необходимо:
# - Использовать 2-3 точечных графика
# - Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
# - Использовать PairGrid с типом графика на ваш выбор
# - Изобразить Heatmap
# - Использовать 2-3 гистограммы

# Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------
penguins = sns.load_dataset("penguins")
penguins.head()
# --------------------------------

penguins.loc[penguins['bill_length_mm'] >= 42, 'high_group'] = 'high'
penguins.loc[(penguins['bill_length_mm'] >= 35) & (penguins['bill_length_mm'] < 42), 'high_group'] = 'middle'
penguins.loc[penguins['bill_length_mm'] < 35, 'high_group'] = 'low'


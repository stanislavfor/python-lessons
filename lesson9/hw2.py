# Задача 2. Узнать какая максимальная households в зоне минимального значения population

import pandas as pd
df = pd.read_csv('..\california_housing_train.csv')

print(df[df['population'] == df['population'].min()].households.max())
# 4.0
# или
print(df[df['population'] == df['population'].min()]['households'].max())
# 4.0
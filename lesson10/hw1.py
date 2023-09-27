#  Задача 1. В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без  get_dummies?

import pandas as pd
import numpy as np

# Используйте этот код, чтобы переписать в формате one hot:
# --------------------------------
import random

def fun():
  while True:
    lst = ['robot '] * 10
    lst += ['human '] * 10
    # lst += ['codes '] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI':lst})
    data.head()
    # # --------------------------------
    # print(data.head())
    # print()

    print('whoAmI', end = "")
    oh = pd.unique(data['whoAmI'])
    df = pd.DataFrame()
    for value in oh: df[value] = (data['whoAmI'] == value)
    df = df.astype(int)
    print(df.head())
    # print(df.head(4))
    input("Press Enter to continue")
fun()
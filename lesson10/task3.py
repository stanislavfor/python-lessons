# Задача 3. 
# 1. Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

# Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------
penguins = sns.load_dataset("penguins")
penguins.head()
# --------------------------------s
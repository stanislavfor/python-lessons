# Знакомство с языком Python (семинары)


## Урок 10. Построение графиков
### Контрольные задачи

#### Задача 1. Выполнить для файлов из лекции:
Ресурс [colab.research.google.com](https://colab.research.google.com/)
1. Изобразите отношение households к population с помощью точечного графика
2. Визуализировать longitude по отношения к median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с оттенком housing_median_age


#### Задача 2. Написать EDA для датасета про пингвинов. Необходимо:
- Использовать 2-3 точечных графика
- Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
- Использовать PairGrid с типом графика на ваш выбор
- Изобразить Heatmap
- Использовать 2-3 гистограммы
#### Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:

```
penguins = sns.load_dataset("penguins")
penguins.head()
```

#### Задача 3. 
1. Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина.

```
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)```

#### Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:

```
penguins = sns.load_dataset("penguins")
penguins.head()
```

#### Задача 4. 
1. Изобразить гистограмму по flipper_length_mm с оттенком height_group. 
Сделать анализ





### Домашняя работа
#### Задача 1. В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без  get_dummies?

```
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
```

[<u>Статья про one hot вид</u>](https://colab.research.google.com/drive/1qKamnDiRmpRZkpiqWPkunBdAhmzhMcGz?usp=sharing)


##### Ссылки на Домашнюю работу:
- [Задача 1.](https://github.com/stanislavfor/python-lessons/blob/main/lesson10/hw1.py)

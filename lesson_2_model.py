import pandas as pd
import glob
import os
import tqdm
import gc
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import seaborn as sns
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import math
from sklearn import datasets, linear_model, model_selection
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix
from tqdm import tqdm

# Загрузка данных и чистка
f = os.path.join(
    "D:\\", "GitHub", "MISIS-Python", "athletes_sochi.txt"
)
dfs = pd.read_csv(f).dropna()

# Подготовка дополнительных полей¶
dfs["BMI"] = dfs["weight"] / (dfs["height"]**2)
myH = 1.83
myW = 75
myBMI = myW/(myH**2)

# набор пар для входных векторов X: пары это вес и рост
# набор пар для выходных векторов Y: это значения 1 -- male, 0 -- female
# перемешать набор данных весь и взять 20% отложить как test, остальное будет train
alldata = dfs[['weight', 'height', 'BMI', 'gender']]
alldata = alldata.sample(frac=1)
# allinput = alldata[ ['weight', 'height'] ] возможно понадобится заменить 
allinput = alldata[['weight', 'height', 'BMI']]
alloutput = alldata["gender"].apply(lambda x: int(x == "Male"))

# Разделим наши выборки
chunk_80 = int(len(alldata) * 0.8)

X_train = allinput[:chunk_80]
Y_train = alloutput[:chunk_80]

X_test = allinput[chunk_80:]
Y_test = alloutput[chunk_80:]
# Тоже самое можно сделать при помощи библиотеки:
# X_train, X_test, Y_train, Y_test = model_selection.train_test_split(allinput, alloutput, test_size=0.2)

# Создаем модель
model = linear_model.LogisticRegression()
# Обучаем модель
print(model.fit(X_train, Y_train))
# Смотрим на коэффициенты
print(model.coef_)

# Предскажем пол
Y_test_predicted = model.predict(X_test)
mysex = model.predict([[myW, myH,  myBMI]])

# Метрики precision и recall
[tn, fp], [fn, tp] = confusion_matrix(Y_test, Y_test_predicted)
confusion_matrix(Y_test, Y_test_predicted)
precision = tp / (tp + fp)
recall = tp / tp + fn

print("Precision: ", tp / (tp + fp))
print("Recall: ", tp / (tp + fn))
print("Accuracy: ", (tn + tp) / (tp + fp + tn + fn))
print("F1: ",  (precision * recall) / ((precision) + recall))

from sklearn.metrics import classification_report
report = classification_report(Y_test, model.predict(X_test), target_names=['Male', 'Female'])
print(report)

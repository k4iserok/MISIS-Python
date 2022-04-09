import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


FILEPATH = 'data/DataSet_w_NA.xlsx'

df = pd.read_excel(FILEPATH, sheet_name="Испорченные факты")
df = df.dropna()
df = pd.pivot_table(df, values=['Продажи, руб', 'Продажи, шт', 'Повторение заказа', 'Маржинальная прибыль', 'Повторение товара'], index=["Факты.Товар ID"],
                    aggfunc={'Продажи, шт': [np.median, np.sum],
                             'Продажи, руб': np.sum,
                             'Повторение заказа': np.sum,
                             'Маржинальная прибыль': np.sum

                             })
newname = df.columns.map('_'.join)
df.columns = newname
df = df.reset_index()
total_sale = df['Продажи, руб_sum'].sum()
df['Доля'] = df['Продажи, руб_sum']/total_sale * 100
df = df.sort_values(by=('Продажи, руб_sum'), ascending=False)
df = df.assign(sum_d=df['Доля'].cumsum())

df.loc[(df['sum_d'] <= 80), 'ABC'] = 'A'
df.loc[(df['sum_d'] > 80) & (df['sum_d'] <= 95), 'ABC'] = 'B'
df.loc[(df['sum_d'] > 95), 'ABC'] = 'C'


df['Стоимость, руб'] = df['Продажи, руб_sum']/df['Продажи, шт_sum']
df['Продажи в следующем периоде, шт'] = (
    df['Продажи, шт_sum'] + df['Продажи, шт_median'])
df['Продажи в следующем периоде'] = (
    df['Продажи, шт_sum'] + df['Продажи, шт_median']) * df['Стоимость, руб']
total_sale_next = df['Продажи в следующем периоде'].sum()
df['Доля_будущая'] = df['Продажи в следующем периоде']/total_sale_next * 100
df = df.sort_values(by=('Продажи в следующем периоде'), ascending=False)
df = df.assign(sum_d_next=df['Доля_будущая'].cumsum())

df.loc[(df['sum_d_next'] <= 80), 'ABC_next'] = 'A'
df.loc[(df['sum_d_next'] > 80) & (df['sum_d_next'] <= 95), 'ABC_next'] = 'B'
df.loc[(df['sum_d_next'] > 95), 'ABC_next'] = 'C'

df = df.sample(frac=1)
X = df[['Стоимость, руб', 'Продажи в следующем периоде, шт']]
y = df['ABC_next']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=20)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))


svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
y_pred_1 = svclassifier.predict(X_test)

print(classification_report(y_test, y_pred_1))


classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred_2 = classifier.predict(X_test)

print(classification_report(y_test, y_pred_2))

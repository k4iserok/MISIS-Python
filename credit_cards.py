# Essentials
# t-SNE visualization
# imputation
# Scaling
# PCA
# K-means for Clustering
# elbow method
# cluster metrics
# Silhouette Visualizer
# ignore warnings
# %%

from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.impute import KNNImputer
from sklearn.manifold import TSNE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

cc_general = pd.read_csv('CC GENERAL.csv')
cc_general.head()
# print(cc_general.describe())

# Проверяем все пустые значения по столбцам
cc_general.isna().sum()

# Найдем выбросы используя IQR(межквартильный размах)
# Для начала вычислим первый и третий квантили Q1 и Q3
# Затем оценим межквартильный размах IQR= Q3 - Q1
# Оцениваем нижнюю и верхнюю границы: minimum и maximum
# Точки данных, лежащие за пределами нижней и верхней границ, являются выбросами.


def outlier_percent(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    minimum = Q1 - (1.5 * IQR)
    maximum = Q3 + (1.5 * IQR)
    num_outliers = np.sum((data < minimum) | (data > maximum))
    num_total = data.count()
    return (num_outliers/num_total)*100


non_categorical_data = cc_general.drop(['CUST_ID'], axis=1)
for column in non_categorical_data.columns:
    data = non_categorical_data[column]
    percent = str(round(outlier_percent(data), 2))
    # print(f'Outliers in "{column}": {percent}%')
# Избавляемся от "шума", для этого устанавливаем все выбросы как NaN
for column in non_categorical_data.columns:
    data = non_categorical_data[column]

    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    minimum = Q1 - (1.5 * IQR)
    maximum = Q3 + (1.5 * IQR)

    outliers = ((data < minimum) | (data > maximum))
    non_categorical_data[column].loc[outliers] = np.nan

# print(non_categorical_data.isna().sum())

# Используем метод KNN
imputer = KNNImputer()
imp_data = pd.DataFrame(imputer.fit_transform(
    non_categorical_data), columns=non_categorical_data.columns)
print(imp_data.isna().sum())

# Scale
std_imp_data = pd.DataFrame(StandardScaler().fit_transform(
    imp_data), columns=imp_data.columns)
# print(std_imp_data.head())

pca = PCA(n_components=0.9, random_state=42)
pca.fit(std_imp_data)
PC_names = ['PC'+str(x) for x in range(1, len(pca.components_)+1)]
pca_data = pd.DataFrame(pca.transform(std_imp_data), columns=PC_names)

fig, ax = plt.subplots(figsize=(24, 16))
plt.imshow(pca.components_.T,
           cmap="Spectral",
           vmin=-1,
           vmax=1,
           )
plt.yticks(range(len(std_imp_data.columns)), std_imp_data.columns)
plt.xticks(range(len(pca_data.columns)), pca_data.columns)
plt.xlabel("Principal Component")
plt.ylabel("Contribution")
plt.title("Contribution of Features to Components")
# plt.colorbar()
# %%
model = KMeans(random_state=42)
distortion_visualizer = KElbowVisualizer(model, k=(2, 10))

distortion_visualizer.fit(pca_data)
distortion_visualizer.show()

km_model = KMeans(distortion_visualizer.elbow_value_, random_state=42)
labels = km_model.fit_predict(pca_data)

cc_general['LABELS'] = labels
std_imp_data['LABELS'] = labels
pca_data['LABELS'] = labels

pca_data.LABELS.value_counts().plot.pie(
    autopct='%1.0f%%', pctdistance=0.7, labeldistance=1.1)


visualizer = SilhouetteVisualizer(km_model, colors='yellowbrick')
visualizer.fit(pca_data.drop(['LABELS'], axis=1))
visualizer.show()


def spider_plot(data, title):
    means = data.groupby("LABELS").mean().to_numpy()
    names = data.columns[0:-1]
    label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(names))
    categories = np.arange(0, len(means))
    plt.figure(figsize=(10, 10))
    plt.subplot(polar=True)
    for i in range(len(means)):
        plt.plot(label_loc, means[i], label=f'class {categories[i]}')
    plt.title(f'Feature comparison ({title})', size=20)
    lines, labels = plt.thetagrids(np.degrees(label_loc), labels=names)
    plt.legend()
    plt.show()


spider_plot(pca_data, 'PCA Data')


def colorful_scatter(data):
    LABEL_COLOR_MAP = {0: 'y',
                       1: 'g',
                       2: 'm',
                       3: 'k'
                       }
    sns.jointplot(data=data, x="BALANCE", y="PURCHASES",
                  hue="LABELS", palette=LABEL_COLOR_MAP, alpha=0.6, height=10)


colorful_scatter(std_imp_data)
# %%

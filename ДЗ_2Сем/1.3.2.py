import pandas as pd
import numpy as np

FILEPATH = 'data/iris.csv'

df = pd.read_csv(FILEPATH)

print('Разброс значений для датасета iris')
dnm = df.groupby('Name').agg(np.ptp)
print(dnm)

import pandas as pd

FILEPATH = 'data/tips.csv'

df = pd.read_csv(FILEPATH)

mask = df['smoker'] == 'Yes'
mask &= df['day'] == 'Fri'
mask &= df['sex'] == 'Male'
mask &= df['time'] == 'Lunch'


print(
    f'В среднем выходит полный счёт по пятницам на ланч у курящих мужчин: \n {df[mask]["total_bill"].mean()}')

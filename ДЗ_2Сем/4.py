import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing

FILEPATH = 'data/tips.csv'

df = pd.read_csv(FILEPATH)

le = preprocessing.LabelEncoder()
df.day = le.fit_transform(df.day)

df['sex'] = df['sex'].apply(lambda x: int(x == "Male"))
df['smoker'] = df['smoker'].apply(lambda x: int(x == "Yes"))
df['time'] = df['sex'].apply(lambda x: int(x == "Dinner"))

X = df.drop('tip', axis=1)
y = df['tip']

X_train, X_test, y_train, y_test = train_test_split(X, y)

regressor = xgb.XGBRegressor(
    n_estimators=100, reg_lambda=1, gamma=0, max_depth=3)

regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(y_pred)
print(mean_squared_error(y_test, y_pred))

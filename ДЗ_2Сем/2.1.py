import pandas as pd
from sklearn import linear_model, model_selection
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

FILEPATH = 'data/athletes_sochi.txt'


def data_class(allinput, alloutput):

    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
        allinput, alloutput, test_size=0.2)
    model = linear_model.LogisticRegression()
    model.fit(X_train, Y_train)

    Y_test_predicted = model.predict(X_test)

    mysex = model.predict([[myAge, myW, myH, myKoef]])

    [tn, fp], [fn, tp] = confusion_matrix(Y_test, Y_test_predicted)

    precision = tp / (tp + fp)
    recall = tp / tp + fn

    print("Precision: ", tp / (tp + fp))
    print("Recall: ", tp / (tp + fn))
    print("Accuracy: ", (tn + tp) / (tp + fp + tn + fn))
    print("F1: ",  (precision * recall) / ((precision) + recall))
    print('Ваш предсказанный пол:')
    if mysex == 1:
        print('Мужчина')
    else:
        print('Женщина')
    report = classification_report(Y_test, model.predict(
        X_test), target_names=['Male', 'Female'])
    print(report)


df = pd.read_csv(FILEPATH).dropna()

df["age_BMI"] = df["age"] / (df["weight"] / (df["height"]**2))
myAge = 23
myW = 75
myH = 1.84
myKoef = myAge / (myW/(myH**2))
alldata = df[['age', 'weight', 'height', 'age_BMI', 'gender']]
alldata = alldata.sample(frac=1)
allinput = alldata[['age', 'weight', 'height', 'age_BMI']]
alloutput = alldata["gender"].apply(lambda x: int(x == "Male"))
data_class(allinput, alloutput)

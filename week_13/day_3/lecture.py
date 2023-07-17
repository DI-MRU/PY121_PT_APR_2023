from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)

import pandas as pd
import numpy as np

# # Linear Regression

# data = pd.read_csv("height_weight.csv")

# X_lin = X = data["Height"].values.reshape(-1, 1)
# y_lin = y = data["Weight"].values.reshape(-1, 1)

# lr = LinearRegression()
# reg = lr.fit(X, y)
# print(reg.coef_, reg.intercept_)

# print(reg.predict([[190.5]]))

# # Logistic Regression

# data = pd.read_csv("height_gender.csv")

# X = data["Height"].values.reshape(-1, 1)
# y = data["Gender"]

# clf = LogisticRegression()
# result = clf.fit(X, y)
# y_test = [[100], [148]]
# print(clf.predict_proba(y_test), clf.predict(y_test))


# X_train, X_test, y_train, y_test = train_test_split(
#     X_lin, y_lin, test_size=0.20, random_state=42
# )

# lr = LinearRegression()
# reg = lr.fit(X_train.reshape((-1, 1)), y_train)

# y_pred = lr.predict(X_test.reshape((-1, 1)))

# print(f"MAE pred: {mean_absolute_error(y_test, y_pred)}")

# #

# y_pred_random = np.random.uniform(
#     low=35, high=120, size=(y_test.size,)
# )  # generate random numbers between 35 and 120 kilograms
# print(f"MAE rand pred: {mean_absolute_error(y_test, y_pred_random)}")

# print(f"MSE pred: {mean_squared_error(y_test, y_pred)}")
# print(f"MSE rand pred: {mean_squared_error(y_test, y_pred_random)}")


# df = pd.read_csv(
#     "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# )

# y = df["species"]
# X = df.drop(
#     ["species"], axis=1
# )  # this function returns a copy of the dataframe with the dropped columns

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# clf = LogisticRegression()
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
# acc = accuracy_score(y_test, y_pred)
# print(f"Accuracy is {acc * 100:.2f}%")

# # --------------------------------------------

# titanic = pd.read_csv(
#     "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
# ).dropna()
# y = titanic["Survived"]
# X = titanic.drop(["Survived"], axis=1)._get_numeric_data()
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
# clf = LogisticRegression(max_iter=10000)
# clf.fit(X_train, y_train)

# y_pred = clf.predict(X_test)
# print(f"Titanic prediction: {y_pred}")
# tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
# print(f"True positives: {tp}")
# print(f"True negatives: {tn}")
# print(f"False positives: {fp}")
# print(f"False negatives: {fn}")
# print(f"Manual Precision: {tp / (tp + fp)}")
# print(f"Precision: {precision_score(y_test, y_pred)}")
# print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
# print(f"Manual Recall: {tp / (tp + fn)}")
# print(f"Recall: {recall_score(y_test, y_pred)}")

# # Tuning

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV

breast_cancer = load_breast_cancer()
hyperparameters = {"C": [0.0007, 0.001, 0.01, 0.2, 1, 10, 100, 200, 500, 5203]}

log = LogisticRegression(max_iter=100000)
gs = GridSearchCV(
    log, hyperparameters, cv=5, n_jobs=-1, scoring="accuracy"
)  # 5 folds, using accuracy metric
gs.fit(breast_cancer.data, breast_cancer.target)

print(gs.cv_results_["mean_test_score"])
# array([0.9279615 , 0.94027325, 0.94025772, 0.94904518, 0.95081509, 0.95081509, 0.95433939])

print(gs.cv_results_["rank_test_score"])
# array([7, 5, 6, 4, 2, 2, 1], dtype=int32)

print(gs.best_score_)


gs = GridSearchCV(
    log, hyperparameters, cv=5, n_jobs=-1, scoring="precision"
)  # 5 folds, using accuracy metric
gs.fit(breast_cancer.data, breast_cancer.target)

print(gs.cv_results_["mean_test_score"])
# array([0.9279615 , 0.94027325, 0.94025772, 0.94904518, 0.95081509, 0.95081509, 0.95433939])

print(gs.cv_results_["rank_test_score"])
# array([7, 5, 6, 4, 2, 2, 1], dtype=int32)

print(gs.best_score_)

gs = GridSearchCV(
    log, hyperparameters, cv=5, n_jobs=-1, scoring="recall"
)  # 5 folds, using accuracy metric
gs.fit(breast_cancer.data, breast_cancer.target)

print(gs.cv_results_["mean_test_score"])
# array([0.9279615 , 0.94027325, 0.94025772, 0.94904518, 0.95081509, 0.95081509, 0.95433939])

print(gs.cv_results_["rank_test_score"])
# array([7, 5, 6, 4, 2, 2, 1], dtype=int32)

print(gs.best_score_)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
)

y = df["species"]
X = df[["petal_length", "petal_width"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

print(X_test.shape)
print(X_train.shape)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

species_list = ["setosa", "versicolor", "virginica"]
markers = ["x", "v", "h"]

matplotlib.use("qtagg")
fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

# Plot the training points
for species, marker in zip(species_list, markers):
    ax[0, 0].scatter(
        X_train[df.species == species]["petal_length"],
        X_train[df.species == species]["petal_width"],
        marker=marker,
    )
ax[0, 0].set_title("Training Data")
ax[0, 0].legend(species_list)

# Plot the predicted points
for species in species_list:
    ax[0, 1].scatter(
        X_test[y_pred == species]["petal_length"],
        X_test[y_pred == species]["petal_width"],
        marker=".",
    )
ax[0, 1].set_title("Predicted Data")
ax[0, 1].legend(
    [
        "setosa_pred",
        "versicolor_pred",
        "virginica_pred",
    ]
)

# Plot both the training and predicted points
for species, marker in zip(species_list, markers):
    ax[1, 0].scatter(
        X_train[df.species == species]["petal_length"],
        X_train[df.species == species]["petal_width"],
        marker=marker,
    )
for species in species_list:
    ax[1, 0].scatter(
        X_test[y_pred == species]["petal_length"],
        X_test[y_pred == species]["petal_width"],
        marker=".",
    )
ax[1, 0].set_title("Training and Predicted Data")
ax[1, 0].legend(
    [
        "setosa",
        "versicolor",
        "virginica",
        "setosa_pred",
        "versicolor_pred",
        "virginica_pred",
    ]
)


# Generate random prediction points with:
# petal_length values between 0 and 7
# petal_width values between 0 and 2.5
data = np.random.rand(100000, 2)
# print(data)
data[:, 0] *= 7
data[:, 1] *= 2.5
new_df = pd.DataFrame(data, columns=["petal_length", "petal_width"])

y_new = knn.predict(new_df)

# Plot the random prediction points
for species in species_list:
    ax[1, 1].scatter(
        new_df[y_new == species]["petal_length"],
        new_df[y_new == species]["petal_width"],
        marker="1",
    )

ax[1, 1].set_title("Random Predicted Data")
ax[1, 1].legend(
    [
        "setosa_pred",
        "versicolor_pred",
        "virginica_pred",
    ]
)

# Add axis labels & display plot
fig.text(0.5, 0.04, "Petal Length", ha="center")
fig.text(0.04, 0.5, "Petal Width", va="center", rotation="vertical")
plt.show()

# (._. ) Why are we doing exercises, Vincent?
#
# *\o/* Because they're FUN!
#
# ( ._.) (._. ) Oh no...

import numpy as np


# Class called KNNClassifier with methods fit() & predict()
# NOTE: Different from Exercises XP requirements, this works with continuous data (i.e. Regression)
class KNNClassifier:
    def __init__(self, k=3):
        """Constructor."""
        self.k = k
        print(f"The KNNClassifier has been created with {k}-NN.")

    def fit(self, training_data):
        """Fit the training data to the model."""
        self.training_data = training_data
        print(f"The KNNClassifier has been trained.")

    def predict(self, prediction_data):
        """Predict the result of a set of input."""

        # Result shaping example
        # Prediction (5, 2) | X, Y
        # Result     (5, 3) | X, Y, Prediction
        results = np.zeros((prediction_data.shape[0], prediction_data.shape[1] + 1))

        index_count = 0
        for data_point in prediction_data:
            distances = []
            closest_pts = []

            # Calculate all distances from the data point
            for train_point in self.training_data:
                dist = np.linalg.norm(data_point - train_point[0:2])
                distances.append(dist)

            # Figure out which training points are closest to the data point
            sorted_indices = np.argsort(distances)
            for j in range(self.k):
                # Find the index of the index 0 in `sorted_indices`
                # Use that index to get the value of the distance in `distances`
                knn_index = np.where(sorted_indices == j)[0][0]
                knn_value = distances[knn_index]
                closest_pts.append(knn_value)

            total = 0
            for x in closest_pts:
                total = total + x
            avg = total / len(closest_pts)

            # Prepare results
            results[index_count][0] = data_point[0]
            results[index_count][1] = data_point[1]
            results[index_count][2] = avg

            index_count = index_count + 1

        print(f"The KNNClassifier has completed its predictions.")
        return results


# Create an object of class KNNClassifier called knn
knn = KNNClassifier()

# Prepare training data
training_data = np.random.rand(1000, 3)
training_data[:, 0] *= 100  # X value
training_data[:, 1] *= 100  # Y value

# Label
training_data[:, 2] *= 1000
training_data[:, 2] = training_data[:, 2] + 1000

knn.fit(training_data)  # Train the model

# Prepare random prediction points & find the result
prediction_data = np.random.rand(100, 2)
predictions = knn.predict(prediction_data)
print(predictions)

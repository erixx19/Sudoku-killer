#Linear regression
#This project demonstrates how machine learning models work under the hood without using any high-level libraries like scikitlearn, etc.
#I'm new and for now I'm exploring the world of ML so, it's just a beginner friednly, tiny project! 

import numpy as np

# Dummy dataset: [Area in sqft], [Price in $1000]
X = np.array([650, 800, 1200, 1500, 1800])
y = np.array([70, 90, 135, 160, 185])

# Normalize data (mean normalization)
X_mean = np.mean(X)
X_std = np.std(X)
X_norm = (X - X_mean) / X_std

# Add bias term (intercept)
X_train = np.c_[np.ones(X.shape[0]), X_norm]

# Initialize weights
theta = np.zeros(2)

# Hyperparameters
alpha = 0.01
epochs = 1000

# Gradient Descent
for epoch in range(epochs):
    y_pred = X_train @ theta
    error = y_pred - y
    gradient = X_train.T @ error / len(X)
    theta -= alpha * gradient

# Unnormalize input for prediction
def predict(area):
    norm_area = (area - X_mean) / X_std
    x_input = np.array([1, norm_area])
    return round(x_input @ theta, 2)

# Test
print("Predicted price for 1000 sqft:", predict(1000), "thousand $")
print("Predicted price for 2000 sqft:", predict(2000), "thousand $")

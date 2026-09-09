import numpy as np

def compute_trajectory_coefficients(x, y, z):
    # O(n) Polynomial Regression
    poly_y = np.polyfit(x, y, 2)
    poly_z = np.polyfit(x, z, 2)
    return np.poly1d(poly_y), np.poly1d(poly_z)

def predict_future_coordinates(fn_y, fn_z, start_x, end_x, intervals=20):
    # O(k) Iterative Evaluation
    future_x = np.linspace(start_x, end_x, intervals)
    future_y = fn_y(future_x)
    future_z = fn_z(future_x)
    return future_x, future_y, future_z
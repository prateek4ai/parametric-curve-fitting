import numpy as np

def parametric_curve(t, theta, M, X):
    """
    Computes x, y coordinates from parametric equations for given t and parameters.
    Args:
        t: array-like, shape (n_points,) -- input parameter
        theta: float (radians)
        M: float
        X: float
    Returns:
        x: np.ndarray (n_points,)
        y: np.ndarray (n_points,)
    """
    t = np.array(t)
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y

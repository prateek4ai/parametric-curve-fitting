import numpy as np
from scipy.optimize import differential_evolution
from .curve_model import parametric_curve

def l1_loss(params, t_data, x_data, y_data):
    """
    Objective function: sum of L1 distances between fitted and observed points.
    params: [theta, M, X] (float)
    t_data: array-like (shape: n,)
    x_data: observed x values
    y_data: observed y values
    """
    theta, M, X = params
    x_fit, y_fit = parametric_curve(t_data, theta, M, X)
    return np.sum(np.abs(x_fit - x_data) + np.abs(y_fit - y_data))


def fit_curve(t_data, x_data, y_data):
    """
    Finds best-fit parameters using differential evolution.
    Returns (theta, M, X), minimum_L1_loss
    """
    # Set bounds: theta (0 to pi/2 radians), M (0.001 to 0.0091), X (10.2 to 14.2)
    bounds = [
        (0, np.pi / 2),    # theta: 0 to 90 degrees in radians
        (0.001, 0.0091),   # M
        (10.2, 14.2)       # X
    ]
    result = differential_evolution(
        l1_loss,
        bounds,
        args=(t_data, x_data, y_data),
        strategy="best1bin",
        maxiter=500,
        popsize=15,
        tol=1e-6,
        polish=True,
        seed=42,
        disp=True
    )
    theta_opt, M_opt, X_opt = result.x
    min_loss = result.fun
    return (theta_opt, M_opt, X_opt), min_loss

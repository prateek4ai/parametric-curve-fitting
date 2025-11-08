import matplotlib.pyplot as plt
import numpy as np

def plot_curve(x_data, y_data, x_fit, y_fit, filename):
    """
    Plots real data points and fitted parametric curve.
    Saves plot to the specified filename (string).
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(x_data, y_data, s=20, color="blue", label="Data Points")
    plt.plot(x_fit, y_fit, color="red", lw=2, label="Fitted Curve")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Parametric Curve Fitting")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

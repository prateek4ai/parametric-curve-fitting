import numpy as np
import pandas as pd
from src.curve_model import parametric_curve
from src.optimizer import fit_curve
from src.visualizer import plot_curve

# 1. Load CSV data
data = pd.read_csv("data/xy_data.csv")  # Make sure your CSV is here, or use your correct filename
t_data = np.linspace(6, 60, len(data))  # Uniformly sample t for the number of data points
x_data = data["x"].values
y_data = data["y"].values

# 2. Optimize parameters and compute minimum L1 loss
print("Fitting parameters, this may take up to 2 minutes...")
(opt_theta, opt_M, opt_X), min_loss = fit_curve(t_data, x_data, y_data)
print("Optimal parameters:")
print(f"  theta = {np.degrees(opt_theta):.4f}° (in radians: {opt_theta:.6f})")
print(f"  M     = {opt_M:.6f}")
print(f"  X     = {opt_X:.6f}")
print(f"Total L1 Loss: {min_loss:.4f}")

# 3. Compute fitted curve
t_fine = np.linspace(6, 60, 1000)
x_fit, y_fit = parametric_curve(t_fine, opt_theta, opt_M, opt_X)

# 4. Plot and save figure
plot_curve(x_data, y_data, x_fit, y_fit, "outputs/fitted_curve.png")

# 5. Output report
with open("outputs/submission_report.txt", "w") as f:
    f.write("Parametric Curve Fitting Results\n")
    f.write(f"Theta (radians): {opt_theta:.6f}\n")
    f.write(f"Theta (degrees): {np.degrees(opt_theta):.4f}\n")
    f.write(f"M: {opt_M:.6f}\n")
    f.write(f"X: {opt_X:.6f}\n")
    f.write(f"Total L1 Loss: {min_loss:.4f}\n")
    f.write("\n---\n")
    f.write("Fitted curve plot saved as outputs/fitted_curve.png\n")

print("\nAll done! Report and figure are in the outputs/ folder.")

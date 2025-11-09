# Parametric Curve Fitting Project

### Fitted Parametric Equations

$$
x = t \cos(0.304676) - e^{0.0091|t|} \cdot \sin(0.3t) \sin(0.304676) + 14.2
$$
$$
y = 42 + t \sin(0.304676) + e^{0.0091|t|} \cdot \sin(0.3t) \cos(0.304676)
$$

### Fitted Parameters

* $\theta = 0.304676$ radians ($17.46^\circ$)
* $M = 0.0091$
* $X = 14.20$

---

### Complete Process and Approaches Used

This project demonstrates parametric curve fitting and model optimization in Python for a set of $(x, y)$ data points. This section details all key steps and rationale behind my choices:

1.  **Understanding the Model**
    The underlying parametric equations feature three unknowns: $\theta$, $M$, and $X$.
    The goal is to fit these parameters so the generated curve best matches the provided dataset over $t$.

2.  **Data Loading & Preparation**
    Loaded the experimental data and verified its integrity and formatting.
    Prepared $t$ values uniformly over the given range, matching the requirements of the parametric shape.

3.  **Fitting Method & Loss Function**
    Selected L1 loss (sum of absolute differences) to ensure the fit is robust to outliers and provides a reliable match to the actual data distribution.
    Defined a function to compute the L1 distance between observed data and predicted curve for parameter optimization.

4.  **Model Fitting & Optimization Strategy**
    Used Python's `scipy.optimize` library with a two-step process:
    * Differential Evolution for initial global searching.
    * L-BFGS-B for efficient local refinement with parameter bounds.
    Set appropriate bounds for $\theta$, $M$, and $X$ to ensure plausible, stable solutions.
    Iteratively refined the fit until the loss was minimized and all constraints were satisfied.

5.  **Diagnostics & Verification**
    Recorded and reported the optimal parameter values and total L1 loss for transparency.
    Generated a plot of the fitted curve (`outputs/fitted_curve.png`) for visual inspection.
    Saved all parameters and results in `outputs/submission_report.txt`.

6.  **Visualization**
    Presented the final parametric equations in LaTeX with substituted parameter values for clarity.
    Provided an interactive Desmos visualization so reviewers can view and manipulate the curve dynamically.

7.  **Documentation and Humanized Summary**
    All steps, choices, and code are fully documented for easy review.
    Project structure ensures reproducibility and transparency, making it easy for others to understand and build upon.

---

### Desmos Visualization

[**View interactive Desmos plot**](https://www.desmos.com/calculator/1lzooixu4a)

>
---

### Directory Structure

├── main.py # Main script for curve fitting and optimization 
├── src/ # Supporting modules for model, optimization, and utilities 
├── outputs/ # Contains fitted_curve.png, submission_report.txt, etc. 
└── README.md # This documentation

### Usage & Submission Notes

* This README summarizes all key steps, fitted equations, parameter values, and visualization link.
* Code, data, and output files are present in their appropriate folders for review and reproducibility.
* The interactive Desmos link above allows for direct visual assessment of the fitted curve.

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
    Three unknowns are present in the underlying parametric equations.: $\theta$, $M$, and $X$.
    Fitting these parameters to produce a curve that best fits the given dataset over $t$ is the aim.

2.**Loading and Preparing Data**
     loaded the experimental data and checked its formatting and integrity.
     prepared $t$ values that meet the parametric shape's constraints uniformly across the specified range.

 3. **The Loss Function and Fitting Method**
     To make sure the fit is resilient to outliers and offers a trustworthy match to the real data distribution, the L1 loss (sum of absolute differences) was chosen.
     For parameter optimization, a function to calculate the L1 distance between observed data and the predicted curve was defined.

 4. **Model Fitting & Optimization Strategy** Utilized a two-step procedure with Python's `scipy.optimize` library:
     * L-BFGS-B for effective local refinement with parameter constraints; Differential Evolution for preliminary global searching.
     To guarantee believable, stable answers, set suitable constraints for $\theta$, $M$, and $X$.
    Iteratively refined the fit until the loss was minimized and all constraints were satisfied.

5. **Verification and Diagnostics**
     For transparency, the ideal parameter values and total L1 loss were noted and published.
     produced a fitted curve plot (`outputs/fitted_curve.png`) for examination.
     All parameters and outcomes were saved in `outputs/submission_report.txt`.

 6. **Visualization**
     For clarity, the final parametric equations with substituted parameter values were presented in LaTeX.
     gave reviewers access to an interactive Desmos graphic so they could see and work with the curve in real time.

 7. **Documentation**
     For ease of review, every procedure, decision, and piece of code is thoroughly documented.
     Reproducibility and transparency are guaranteed by project structure, which makes it simple for others to comprehend and expand upon.

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

All important procedures, fitted equations, parameter values, and a visualization link are compiled in this README.  For review and repeatability, code, data, and output files are located in the proper directories.  Direct visual evaluation of the fitted curve is possible with the interactive Desmos link mentioned above.

# MSc Big Data Analytics - Advanced Learning (Linear Algebra & ML Practicals)

Repository containing all practical implementations, mathematical notes, and interactive web tools for MSc Big Data Analytics (Advanced Learning).

---

## 📑 Practicals Overview

| Practical | Topic | Implementation & Methods |
| :--- | :--- | :--- |
| **Practical 1** | **Matrix Operations & Image Processing** | Vector/Matrix creation, addition, subtraction, dot product, transpose, determinant, inverse, identity matrix, image brightening/darkening, flipping, and noise using NumPy & Scikit-Image. |
| **Practical 2A** | **Gaussian Elimination** | Solving systems of 3 simultaneous linear equations from scratch with forward elimination and back substitution. |
| **Practical 2B** | **LU Decomposition / Factorization** | Matrix decomposition ($PA = LU$) using `scipy.linalg` (`lu`, `lu_factor`, `lu_solve`), interactive equations, and CSV datasets. |
| **Practical 3** | **Simple Linear Regression** | Mathematical formulas (OLS slope & intercept) vs `scikit-learn` `LinearRegression`, evaluation with $R^2$ score and MSE, applied to `Housing.csv`. |
| **Practical 4** | **Principal Component Analysis (PCA)** | Unsupervised dimensionality reduction from scratch: mean-centering, covariance matrix, eigenvalues/eigenvectors with `np.linalg.eigh`, descending sort, and projection (Iris dataset 4D $\rightarrow$ 2D). |
| **Practical 5** | **Singular Value Decomposition (SVD)** | Low-rank matrix approximation ($A_r = U_r \Sigma_r V_r^T$) for grayscale image compression and Mean Squared Error evaluation across ranks $r \in [5, 1100]$. |
| **Practical 6** | **K-Means Clustering** | Unsupervised clustering from scratch supporting both **Euclidean ($L_2$)** and **Manhattan ($L_1$)** distance metrics, centroid convergence checking (`np.allclose`), and 2D visualization with Matplotlib. |

---

## 🚀 Interactive Copy Web App
Open `index.html` in any web browser to view the interactive practical dashboard with **1-click clipboard copy buttons** for all individual code cells and full practical scripts.

---

## 🛠️ Files in this Repository
* `all_practicals_1_to_6.py` — All practicals combined into a single master script.
* `practical_1.py` to `practical_6.py` — Standalone Python files for each lab practical.
* `index.html` — Interactive web application.
* `MSc_BDA_AL-26-27/` — Original lab submission PDFs.

import os
import json

root = r'c:\Users\asdf\Downloads\MSc_BDA_AL-'
asm_dir = os.path.join(root, 'asm')

practicals_meta = [
    {
        "id": "asm1",
        "title": "Practical 1",
        "topic": "Descriptive Statistics & Exploratory Data Analysis (EDA)",
        "curl_da": "da.gd/s_asm1",
        "curl_is": "is.gd/sid_1",
        "questions": [
            {
                "num": "Q1) Analyze the Iris Dataset",
                "bullets": [
                    "Load the Iris Dataset (150 rows, 4 numerical features).",
                    "Calculate Mean, Median, Mode(s), Standard Deviation, Variance, Skewness, Kurtosis for each numerical feature.",
                    "Plot distribution histograms with KDE (15 bins) in a 2x2 grid.",
                    "Provide detailed statistical analysis: Sepal Length, Sepal Width, Petal Length (Bimodal platykurtic clustering), and Petal Width."
                ]
            },
            {
                "num": "Q2) Analyze the Tips Dataset",
                "bullets": [
                    "Load the Tips Dataset (244 rows, 7 columns).",
                    "Calculate summary statistics for total_bill, tip, size.",
                    "Plot distribution histograms with KDE.",
                    "Analyze customer billing & tipping behaviors (right-skewed bills, round-number tip clustering)."
                ]
            },
            {
                "num": "Q3) Analyze the Indian Stock Market Dataset",
                "bullets": [
                    "Load 'indian_stock_market.csv' (2306 rows).",
                    "Calculate summary statistics for MSFT, IBM, SBUX, AAPL, GSPC using nan_policy='omit'.",
                    "Plot 3x2 grid of distribution histograms with KDE."
                ]
            }
        ],
        "interpretation": "Mean vs Median reveals skewness: right-skewed data (tips and bills) has Mean > Median with long positive tails. Petal measurements exhibit bimodal/platykurtic shapes due to distinct flower sub-species."
    },
    {
        "id": "asm2",
        "title": "Practical 2",
        "topic": "Probability Distributions (Normal, Binomial, Poisson)",
        "curl_da": "da.gd/s_asm2",
        "curl_is": "is.gd/sid_2",
        "questions": [
            {
                "num": "Q1) Normal Distribution X ~ N(70, 10^2)",
                "bullets": [
                    "Generate values of X from 20 to 120 and calculate PDF of X ~ N(70, 10^2).",
                    "Observe: Distribution is symmetric, centered at 70; increasing standard deviation increases spread."
                ]
            },
            {
                "num": "Q2) Effect of Standard Deviation (sigma = 5, 10, 15)",
                "bullets": [
                    "Fix mean = 70. Plot three normal curves for sigma = 5, 10, 15.",
                    "Observe: sigma = 5 is most concentrated; sigma = 15 has greatest spread; height decreases as sigma increases."
                ]
            },
            {
                "num": "Q3) Effect of Mean (mu = 50, 70, 90)",
                "bullets": [
                    "Fix sigma = 10. Plot normal curves for mu = 50, 70, 90.",
                    "Observe: Shift of origin horizontally to the right with no change in scale, spread, or height."
                ]
            },
            {
                "num": "Q4) Binomial Distribution (n = 20, p = 0.3)",
                "bullets": [
                    "Model 20 customers with purchase probability p = 0.3.",
                    "Calculate and plot the Probability Mass Function (PMF) using a stem plot."
                ]
            },
            {
                "num": "Q5) Poisson Distribution (lambda = 4)",
                "bullets": [
                    "Model customer support center receiving average 4 calls per minute.",
                    "Calculate and plot PMF over x = 0 to 14. Confirm lambda = 4, distribution is discrete, expected calls = 4."
                ]
            }
        ],
        "interpretation": "Continuous distributions (Normal) use PDF where area under curve = probability. Discrete distributions (Binomial, Poisson) use PMF where stems show exact integer probabilities."
    },
    {
        "id": "asm3",
        "title": "Practical 3",
        "topic": "Confidence Intervals & Bootstrapping",
        "curl_da": "da.gd/s_asm3",
        "curl_is": "is.gd/sid_3",
        "questions": [
            {
                "num": "Question 1: Parametric Student's t-based 95% Confidence Interval",
                "bullets": [
                    "Given 20 delivery times: [31, 28, 35, 42, 30, 27, 39, 33, 29, 45, 34, 31, 38, 26, 32, 41, 30, 36, 29, 37].",
                    "Compute Sample Mean, Sample SD (ddof=1), Degrees of Freedom (df = 19), Standard Error (SE = s / sqrt(n)).",
                    "Compute 95% Confidence Interval: margin_error = t_critical * SE; lower = mean - margin_error, upper = mean + margin_error."
                ]
            },
            {
                "num": "Question 2: Non-Parametric Bootstrap 95% Confidence Interval",
                "bullets": [
                    "Resample 20 delivery times with replacement 5,000 times (random seed 42) and record sample means.",
                    "Calculate 95% percentile bootstrap CI using 2.5th and 97.5th percentiles.",
                    "Compare t-based CI width vs bootstrap CI width."
                ]
            }
        ],
        "interpretation": "Both t-distribution and 5,000-resample Bootstrap methods produce closely aligned 95% confidence intervals, proving reliable estimation of the true population delivery time."
    },
    {
        "id": "asm4",
        "title": "Practical 4",
        "topic": "Hypothesis Testing (t-test, Chi-Square, ANOVA & Tukey HSD)",
        "curl_da": "da.gd/s_asm4",
        "curl_is": "is.gd/sid_4",
        "questions": [
            {
                "num": "Question 1: Independent Two-Sample t-Test (Fare by Sex)",
                "bullets": [
                    "H0: Mean fare paid by male and female passengers differs insignificantly.",
                    "H1: Mean fare paid by male and female passengers differs significantly.",
                    "Run Welch's t-test (equal_var=False) on Titanic fares: p-value < 0.05 -> Reject H0."
                ]
            },
            {
                "num": "Question 2: Chi-Square Test of Independence (Class vs Survival)",
                "bullets": [
                    "H0: Passenger class and survival status are not associated.",
                    "H1: Passenger class and survival status are associated.",
                    "Run chi2_contingency on crosstab: p-value = 4.55e-23 -> Reject H0."
                ]
            },
            {
                "num": "Question 3: One-Way ANOVA & Post-Hoc Tukey HSD",
                "bullets": [
                    "H0: Mean fares do not differ significantly across the three passenger classes.",
                    "Perform One-Way ANOVA (f_oneway).",
                    "Perform Tukey HSD: First and Second & First and Third fares differ significantly; Second and Third do not."
                ]
            }
        ],
        "interpretation": "1) Females paid significantly higher fares (p < 0.001). 2) Passenger class and survival are strongly dependent. 3) ANOVA confirms fare differences; Tukey HSD shows 1st class differed significantly from 2nd and 3rd, while 2nd and 3rd did not."
    },
    {
        "id": "asm5",
        "title": "Practical 5",
        "topic": "A/B Testing Analysis",
        "curl_da": "da.gd/s_asm5",
        "curl_is": "is.gd/sid_5",
        "questions": [
            {
                "num": "Question: A/B Testing with Two-Sample Welch's t-Test",
                "bullets": [
                    "H0: Means for both groups are the same. H1: Means for both groups are not the same.",
                    "Control Group A (20 obs): [42, 38, 45, 51, 47, 39, 44, 50, 46, 41, 43, 48, 37, 49, 45, 40, 52, 44, 46, 43]",
                    "Treatment Group B (20 obs): [48, 52, 55, 49, 58, 51, 54, 56, 50, 53, 57, 49, 55, 52, 59, 54, 51, 56, 53, 55]",
                    "Calculate sample means, conduct Welch's t-test (equal_var=False).",
                    "Automate decision rule: Reject H0 if p-value < 0.05."
                ]
            }
        ],
        "interpretation": "Mean A = 44.35, Mean B = 53.45. t-statistic = -7.95, p-value = 1.69e-09. Since p < 0.05, we reject H0; Treatment Variant B demonstrates a statistically significant improvement."
    },
    {
        "id": "asm6",
        "title": "Practical 6",
        "topic": "Linear Regression & Spearman Correlation",
        "curl_da": "da.gd/s_asm6",
        "curl_is": "is.gd/sid_6",
        "questions": [
            {
                "num": "Question 1: Simple Linear Regression",
                "bullets": [
                    "Load Diabetes dataset. Compute Pearson correlation: r = 0.5865 (moderate positive relationship).",
                    "Fit OLS Simple Linear Regression: target ~ bmi + intercept (sm.add_constant).",
                    "Regression Equation: Y = 152.1335 + 949.4353(BMI), R^2 = 0.3439 (BMI explains 34.39% of variance)."
                ]
            },
            {
                "num": "Question 2: Multiple Linear Regression",
                "bullets": [
                    "Fit Multiple OLS: target ~ bmi + bp + age.",
                    "R^2 = 0.396, Adjusted R^2 = 0.392.",
                    "Significant predictors: BMI (p < 0.001) and BP (p < 0.001) are significant; Age (p = 0.685) is not significant.",
                    "Equation: Y = 152.1335 + 788.7827(BMI) + 394.1271(BP) + 25.9904(Age)."
                ]
            },
            {
                "num": "Question 3: Spearman Rank Correlation",
                "bullets": [
                    "Given study_time = [2, 4, 1, 5, 3] and exam_score = [50, 65, 45, 80, 60].",
                    "Spearman's rho = 1.0, p-value = 1.40e-24 -> Study Time and Exam score are perfectly positively correlated."
                ]
            }
        ],
        "interpretation": "BMI and BP are statistically significant predictors of disease progression, while Age contributes no significant marginal explanatory power once BMI and BP are in the model."
    },
    {
        "id": "asm7",
        "title": "Practical 7",
        "topic": "Logistic Regression & Classification Metrics",
        "curl_da": "da.gd/s_asm7",
        "curl_is": "is.gd/sid_7",
        "questions": [
            {
                "num": "Question 1: Customer Churn Prediction using Logistic Regression",
                "bullets": [
                    "Load 'scikit-learn/churn-prediction' dataset.",
                    "Predict 'Churn' (0=No, 1=Yes) using 'tenure' and 'MonthlyCharges'.",
                    "80-20 stratified train/test split. Output Confusion Matrix, Accuracy, Precision, Recall, F1-Score, Classification Report.",
                    "Plot ROC curve and compute AUC score (AUC = 0.810)."
                ]
            },
            {
                "num": "Question 2: Palmer Penguins Binary Classification Pipeline",
                "bullets": [
                    "Filter for species Adelie and Gentoo.",
                    "Features: bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g.",
                    "Pipeline with StandardScaler + LogisticRegression(max_iter=1000).",
                    "Evaluate with Confusion Matrix, Performance Metrics, and ROC curve (AUC = 1.000)."
                ]
            }
        ],
        "interpretation": "Churn prediction achieves 77.4% accuracy with AUC = 0.810 (strong predictive capability). Penguin pipeline achieves 100% accuracy (AUC = 1.00) because Adelie and Gentoo are linearly separable across body mass and flipper length dimensions."
    },
    {
        "id": "asm8",
        "title": "Practical 8",
        "topic": "Principal Component Analysis (PCA)",
        "curl_da": "da.gd/s_asm8",
        "curl_is": "is.gd/sid_8",
        "questions": [
            {
                "num": "Question 1 & 2: PCA on Wine Dataset",
                "bullets": [
                    "Load Wine dataset (178 rows, 13 features). Standardize with StandardScaler.",
                    "Compute Explained Variance Ratio and Cumulative Explained Variance.",
                    "Find components explaining >= 90% variance (8 components retain 92.0% variance).",
                    "Plot 2D scatter plot of first two principal components colored by wine class."
                ]
            },
            {
                "num": "Question 3: PCA on Breast Cancer Dataset",
                "bullets": [
                    "Load Breast Cancer dataset (569 observations, 30 features). Standardize with StandardScaler.",
                    "Apply PCA and determine components explaining >= 90% variance (7 components retain 91.0% variance).",
                    "Reduced dataset shape: (569, 7)."
                ]
            }
        ],
        "interpretation": "PCA successfully compresses Wine features from 13 down to 8 (and reveals 3 clear clusters in 2D), and Breast Cancer features from 30 down to 7 components while retaining over 90% of total variance."
    },
    {
        "id": "asm9",
        "title": "Practical 9",
        "topic": "Bayesian Updating for Medical Diagnostic Testing",
        "curl_da": "da.gd/s_asm9",
        "curl_is": "is.gd/sid_9",
        "questions": [
            {
                "num": "Question: Sequential Medical Diagnostic Testing with Bayes' Theorem",
                "bullets": [
                    "Prior disease prevalence: P(Disease) = 0.01 (1%).",
                    "Test Sensitivity: P(+ | Disease) = 0.95 (95%).",
                    "Test Specificity: P(- | No Disease) = 0.90 (90%) -> False Positive Rate = 0.10 (10%).",
                    "1. Compute total probability of positive test: P(+) = 10.85%.",
                    "2. Compute Posterior probability after FIRST positive test: P(D | +) = 8.76%.",
                    "3. Sequential Update: Use first posterior as NEW PRIOR and compute Posterior probability after a SECOND positive test: P(D | +2) = 48.33%!"
                ]
            }
        ],
        "interpretation": "A single positive test only yields an 8.76% probability of actually having the disease due to the Base-Rate Fallacy (1% prevalence). However, undergoing a SECOND independent positive test jumps the posterior probability from 8.76% to 48.33%!"
    }
]

code_dict = {}
for p in practicals_meta:
    num = p["id"].replace("asm", "")
    with open(os.path.join(asm_dir, f'asm_{num}.py'), 'r', encoding='utf-8') as f:
        code_dict[p["id"]] = f.read()

with open(os.path.join(asm_dir, 'all_asm_practicals.py'), 'r', encoding='utf-8') as f:
    code_dict["asm_all"] = f.read()

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MSc BDA - Applied Statistical Methods (ASM Practicals 1-9)</title>
  <style>
    :root {
      --bg-primary: #070b14;
      --bg-secondary: #0f172a;
      --bg-card: #151e33;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-hover: #0284c7;
      --code-bg: #030712;
      --border: #1e293b;
      --border-card: #223254;
      --success: #10b981;
      --purple: #a855f7;
      --purple-hover: #9333ea;
      --amber: #f59e0b;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background-color: var(--bg-primary); color: var(--text-main); display: flex; min-height: 100vh; }

    /* Sidebar */
    .sidebar {
      width: 310px;
      background-color: var(--bg-secondary);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      position: fixed;
      top: 0; bottom: 0; left: 0;
      z-index: 100;
    }

    .sidebar-header {
      padding: 18px 16px;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(135deg, #0f172a, #070b14);
    }
    .sidebar-header h1 { font-size: 1.15rem; color: var(--accent); margin-bottom: 4px; font-weight: 700; }
    .sidebar-header p { font-size: 0.78rem; color: var(--text-muted); }

    .switch-banner {
      display: inline-block;
      margin-top: 10px;
      padding: 6px 12px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 6px;
      color: var(--accent);
      text-decoration: none;
      font-size: 0.8rem;
      font-weight: 600;
      transition: all 0.2s;
    }
    .switch-banner:hover { background: rgba(56, 189, 248, 0.25); color: #fff; }

    .nav-list { list-style: none; overflow-y: auto; flex-grow: 1; padding: 10px 8px; }
    .nav-item {
      padding: 10px 12px;
      margin-bottom: 4px;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      color: #cbd5e1;
      font-size: 0.85rem;
      transition: all 0.2s;
      border: 1px solid transparent;
    }
    .nav-item:hover { background-color: #1e293b; color: #fff; }
    .nav-item.active { background-color: rgba(56, 189, 248, 0.15); border-color: var(--accent); color: var(--accent); font-weight: 600; }
    .nav-item-sub { font-size: 0.72rem; color: var(--text-muted); margin-top: 2px; }

    .mega-btn-wrap { padding: 14px 12px; border-top: 1px solid var(--border); background-color: var(--bg-secondary); }
    .btn-mega {
      width: 100%;
      background: linear-gradient(135deg, var(--purple), var(--purple-hover));
      color: white;
      border: none;
      padding: 12px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.88rem;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(168, 85, 247, 0.35);
      transition: all 0.2s;
    }
    .btn-mega:hover { transform: translateY(-1px); box-shadow: 0 6px 18px rgba(168, 85, 247, 0.5); }

    /* Main Content */
    .content { margin-left: 310px; padding: 32px 40px; flex-grow: 1; max-width: 1250px; }

    /* Cheat Sheet Box */
    .cheat-box {
      background: var(--bg-card);
      border: 1px solid var(--border-card);
      border-radius: 12px;
      padding: 22px;
      margin-bottom: 35px;
    }
    .cheat-box h3 { color: var(--amber); font-size: 1.15rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
    .cheat-table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
    .cheat-table th, .cheat-table td { padding: 11px 12px; text-align: left; border-bottom: 1px solid var(--border); }
    .cheat-table th { color: var(--accent); font-weight: 600; }
    .code-pill {
      background: #020617;
      padding: 4px 9px;
      border-radius: 6px;
      border: 1px solid #1e293b;
      color: #38bdf8;
      font-family: monospace;
      font-size: 0.85rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .code-pill:hover { background: #0f172a; border-color: var(--accent); color: #fff; }

    /* Code Card */
    .code-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-card);
      border-radius: 12px;
      overflow: hidden;
      margin-bottom: 40px;
    }
    .card-head {
      background-color: #0f172a;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-card);
    }
    .card-head-title { font-weight: 700; font-size: 1.1rem; color: #f8fafc; }

    /* Question Box */
    .question-box {
      background: rgba(245, 158, 11, 0.05);
      border-left: 4px solid var(--amber);
      border-bottom: 1px solid var(--border-card);
      padding: 16px 20px;
    }
    .question-badge {
      display: inline-block;
      background: rgba(245, 158, 11, 0.2);
      color: var(--amber);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }
    .q-item { margin-bottom: 12px; }
    .q-item:last-child { margin-bottom: 0; }
    .q-title { font-weight: 600; color: #fde68a; font-size: 0.92rem; margin-bottom: 4px; }
    .q-bullets { list-style: disc; padding-left: 20px; color: #cbd5e1; font-size: 0.85rem; line-height: 1.5; }

    /* Interpretation Box */
    .interp-box {
      background: rgba(56, 189, 248, 0.05);
      border-top: 1px solid var(--border-card);
      border-left: 4px solid var(--accent);
      padding: 14px 20px;
      font-size: 0.85rem;
      color: #cbd5e1;
      line-height: 1.5;
    }
    .interp-title { font-weight: 700; color: var(--accent); margin-bottom: 4px; }

    .btn-copy {
      background-color: #1e293b;
      color: #f1f5f9;
      border: 1px solid var(--border-card);
      padding: 7px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.82rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .btn-copy:hover { background-color: var(--accent); color: #070b14; }

    pre {
      background-color: var(--code-bg);
      padding: 20px;
      overflow-x: auto;
      font-family: "Consolas", "Courier New", monospace;
      font-size: 0.88rem;
      line-height: 1.5;
      color: #e2e8f0;
      max-height: 600px;
    }

    /* Toast */
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--success);
      color: #070b14;
      padding: 12px 20px;
      border-radius: 8px;
      font-weight: 700;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 1000;
    }
    .toast.show { transform: translateY(0); opacity: 1; }
  </style>
</head>
<body>

  <!-- Sidebar -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <h1>📊 ASM Practicals</h1>
      <p>Applied Statistical Methods • Practicals 1-9</p>
      <a href="index.html" class="switch-banner">⚡ Switch to AL Practicals</a>
    </div>

    <ul class="nav-list">
      <li class="nav-item active" onclick="scrollToSec('cheat-sheet')">
        <span>⚡ Quick Curl Cheat Sheet</span>
        <span class="nav-item-sub">One-click Jupyter copy</span>
      </li>
"""

for p in practicals_meta:
    html_content += f"""      <li class="nav-item" onclick="scrollToSec('{p['id']}')">
        <span>{p['title']}</span>
        <span class="nav-item-sub">{p['topic']}</span>
      </li>
"""

html_content += f"""    </ul>

    <div class="mega-btn-wrap">
      <button class="btn-mega" onclick="copyCode('asm_all')">📋 Copy ALL ASM (1 to 9)</button>
    </div>
  </aside>

  <!-- Main Content -->
  <main class="content">

    <!-- Cheat Sheet Section -->
    <section id="cheat-sheet" class="cheat-box">
      <h3>⚡ Jupyter Notebook Quick Copy (Type in Cell)</h3>
      <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 14px;">
        Run any of these in a Jupyter cell to instantly copy that practical's ditto question and code into your clipboard (then press Ctrl + V to paste):
      </p>
      <table class="cheat-table">
        <thead>
          <tr>
            <th>Practical</th>
            <th>Primary Command</th>
            <th>Short Alternative</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background: rgba(168, 85, 247, 0.1);">
            <td><strong>ALL Practicals (1-9)</strong></td>
            <td><code class="code-pill" onclick="copyText('!curl -sL is.gd/sid_all | clip')">!curl -sL is.gd/sid_all | clip</code></td>
            <td><code class="code-pill" onclick="copyText('!curl -sL da.gd/s_asm0 | clip')">!curl -sL da.gd/s_asm0 | clip</code></td>
            <td><button class="btn-copy" onclick="copyCode('asm_all')">Copy All</button></td>
          </tr>
"""

for p in practicals_meta:
    html_content += f"""          <tr>
            <td><strong>{p['title']}</strong> ({p['topic']})</td>
            <td><code class="code-pill" onclick="copyText('!curl -sL {p['curl_is']} | clip')">!curl -sL {p['curl_is']} | clip</code></td>
            <td><code class="code-pill" onclick="copyText('!curl -sL {p['curl_da']} | clip')">!curl -sL {p['curl_da']} | clip</code></td>
            <td><button class="btn-copy" onclick="copyCode('{p['id']}')">Copy</button></td>
          </tr>
"""

html_content += """        </tbody>
      </table>
    </section>

    <!-- Practical Sections -->
"""

for p in practicals_meta:
    code_raw = code_dict[p["id"]].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    # Generate question HTML
    q_html = ""
    for q in p["questions"]:
        bullets_html = "".join([f"<li>{b}</li>" for b in q["bullets"]])
        q_html += f"""
        <div class="q-item">
          <div class="q-title">{q['num']}</div>
          <ul class="q-bullets">{bullets_html}</ul>
        </div>
        """

    html_content += f"""    <section id="{p['id']}" class="code-card">
      <div class="card-head">
        <div>
          <div class="card-head-title">{p['title']} — {p['topic']}</div>
          <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 3px;">
            Jupyter: <code class="code-pill" onclick="copyText('!curl -sL {p['curl_is']} | clip')">!curl -sL {p['curl_is']} | clip</code>
          </div>
        </div>
        <button class="btn-copy" onclick="copyCode('{p['id']}')">📋 Copy Code &amp; Questions</button>
      </div>

      <!-- Full Question Statement -->
      <div class="question-box">
        <span class="question-badge">❓ Full Question Statement</span>
        {q_html}
      </div>

      <!-- Code Block -->
      <pre><code>{code_raw}</code></pre>

      <!-- Key Interpretation -->
      <div class="interp-box">
        <div class="interp-title">💡 Key Result &amp; Interpretation:</div>
        <div>{p['interpretation']}</div>
      </div>
    </section>
"""

html_content += f"""  </main>

  <div id="toast" class="toast">✓ Copied to clipboard!</div>

  <script>
    const codeData = {json.dumps(code_dict)};

    function copyCode(key) {{
      const text = codeData[key];
      if (!text) return;
      navigator.clipboard.writeText(text).then(() => {{
        showToast(key === 'asm_all' ? '✓ ALL ASM Practicals (1-9) Copied!' : '✓ ' + key.toUpperCase() + ' Code & Questions Copied!');
      }});
    }}

    function copyText(str) {{
      navigator.clipboard.writeText(str).then(() => {{
        showToast('✓ Command copied: ' + str);
      }});
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {{ toast.classList.remove('show'); }}, 2500);
    }}

    function scrollToSec(id) {{
      const el = document.getElementById(id);
      if (el) {{
        el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
        event.currentTarget.classList.add('active');
      }}
    }}
  </script>
</body>
</html>
"""

with open(os.path.join(root, 'asm.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Regenerated asm.html with asm new ditto questions! Size:", len(html_content))

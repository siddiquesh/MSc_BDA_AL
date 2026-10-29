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
                    "1. Load the Iris Dataset (150 rows, 4 numerical features).",
                    "2. Calculate Mean, Median, Mode(s) for each numerical feature.",
                    "3. Calculate Standard Deviation and Variance for each numerical feature.",
                    "4. Calculate Skewness and Kurtosis for each numerical feature.",
                    "5. Plot the distribution (histogram with KDE, 15 bins) for each feature.",
                    "6. Interpret the results (symmetry, spreads, outliers)."
                ]
            },
            {
                "num": "Q2) Analyze the Tips Dataset",
                "bullets": [
                    "1. Load the Tips Dataset (244 rows, 7 columns).",
                    "2. Calculate summary statistics (Mean, Median, Mode, Std Dev, Variance, Skewness, Kurtosis) for total_bill, tip, size.",
                    "3. Plot histograms with KDE for all numerical features.",
                    "4. Interpret the results (right-skewed bills & tips)."
                ]
            },
            {
                "num": "Q3) Analyze the Indian Stock Market Dataset",
                "bullets": [
                    "1. Load 'indian_stock_market.csv' (2306 rows).",
                    "2. Calculate statistical moments for MSFT, IBM, SBUX, AAPL, GSPC.",
                    "3. Plot 3x2 grid of distribution histograms with KDE.",
                    "4. Interpret the volatility (variance) and skewness across stocks."
                ]
            }
        ],
        "interpretation": "Mean vs Median reveals skewness: right-skewed data (like tips and stock prices) has Mean > Median with long positive tails. Petal measurements exhibit bimodal/platykurtic shapes due to distinct flower sub-species."
    },
    {
        "id": "asm2",
        "title": "Practical 2",
        "topic": "Probability Distributions (Normal, Binomial, Poisson)",
        "curl_da": "da.gd/s_asm2",
        "curl_is": "is.gd/sid_2",
        "questions": [
            {
                "num": "Q1) Normal Distribution",
                "bullets": [
                    "Plot a Normal Distribution with mean (mu) = 70 and standard deviation (sigma) = 10 over x in [20, 120].",
                    "Observe: Bell curve is symmetric and centered exactly around 70."
                ]
            },
            {
                "num": "Q2) Effect of Standard Deviation on Normal Distribution",
                "bullets": [
                    "Fix mean mu = 70. Plot three normal curves with sigma = 5, 10, 15.",
                    "Observe: sigma = 5 is most concentrated/tallest; sigma = 15 has greatest spread/flattest."
                ]
            },
            {
                "num": "Q3) Effect of Mean on Normal Distribution",
                "bullets": [
                    "Fix sigma = 10. Plot three normal curves with means mu = 50, 70, 90.",
                    "Observe: Normal curve shifts horizontally along x-axis without changing shape or height."
                ]
            },
            {
                "num": "Q4) Binomial Distribution",
                "bullets": [
                    "Plot the PMF of a Binomial Distribution for n = 20 customers with purchase probability p = 0.3.",
                    "Observe: Discrete probabilities peaking around expected value E[X] = n * p = 6."
                ]
            },
            {
                "num": "Q5) Poisson Distribution",
                "bullets": [
                    "Plot the PMF of a Poisson Distribution with average arrival rate lambda = 4 calls per minute over x = 0 to 14.",
                    "Observe: Discrete counts with highest probability around lambda = 4 calls."
                ]
            }
        ],
        "interpretation": "Continuous distributions (Normal) use PDF where area = probability. Discrete distributions (Binomial, Poisson) use PMF where stems show exact event probabilities."
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
                    "Given 20 delivery times: [31, 28, 35, 42, 30, 27, 39, 33, 26, 32, 34, 31, 38, 26, 32, 41, 30, 36, 29, 37].",
                    "Calculate sample mean, sample standard deviation (ddof=1), and degrees of freedom (df = 19).",
                    "Calculate Standard Error: SE = s / sqrt(n).",
                    "Compute 95% CI using Student's t critical value: CI = sample_mean +/- (t_crit * SE)."
                ]
            },
            {
                "num": "Question 2: Non-Parametric Bootstrap 95% Confidence Interval",
                "bullets": [
                    "Resample 20 delivery times with replacement 5,000 times (random seed 42) and compute mean of each bootstrap sample.",
                    "Extract 2.5th and 97.5th percentiles to obtain empirical 95% Bootstrap CI.",
                    "Compare interval estimates and interval widths between t-based and Bootstrap methods."
                ]
            }
        ],
        "interpretation": "Both t-distribution (30.60 to 35.10) and 5,000-resample Bootstrap (30.85 to 35.00) produce tightly matching 95% confidence intervals, proving robust estimation of average delivery time."
    },
    {
        "id": "asm4",
        "title": "Practical 4",
        "topic": "Hypothesis Testing (t-test, Chi-Square, ANOVA & Tukey HSD)",
        "curl_da": "da.gd/s_asm4",
        "curl_is": "is.gd/sid_4",
        "questions": [
            {
                "num": "Question 1: Two-Sample Independent t-Test",
                "bullets": [
                    "Using the Titanic dataset, run Welch's independent t-test (equal_var=False) comparing ticket fares paid by male vs female passengers.",
                    "Hypothesis: H0 (Mean fare male == Mean fare female) vs H1 (Fares differ significantly)."
                ]
            },
            {
                "num": "Question 2: Chi-Square Test of Independence",
                "bullets": [
                    "Build a cross-tabulation matrix of passenger class (First, Second, Third) vs survived (0, 1).",
                    "Perform Chi-Square test of independence (chi2_contingency) to test if survival is independent of class."
                ]
            },
            {
                "num": "Question 3: One-Way ANOVA & Post-Hoc Tukey HSD",
                "bullets": [
                    "Test H0: Mean fares do not differ significantly across the three passenger classes (First, Second, Third).",
                    "Conduct One-Way ANOVA (f_oneway).",
                    "Perform Tukey's Honestly Significant Difference (HSD) post-hoc test to see which specific pairs differ."
                ]
            }
        ],
        "interpretation": "1) Females paid significantly higher fares (p = 5.39e-07). 2) Class and survival are strongly dependent (chi2 = 102.89, p = 4.55e-23). 3) ANOVA confirms fare differences (F = 242.34); Tukey HSD proves First class differs significantly from 2nd and 3rd, while Second and Third classes do not differ significantly (reject=False, p-adj = 0.108)."
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
                    "Control Group A (20 obs): [42, 38, 45, 51, 47, 39, 44, 50, 46, 41, 43, 48, 37, 49, 45, 40, 52, 44, 46, 43]",
                    "Treatment Group B (20 obs): [48, 52, 55, 49, 58, 51, 54, 56, 50, 53, 57, 49, 55, 52, 59, 54, 51, 56, 53, 55]",
                    "1. Compute sample mean for Group A and Group B.",
                    "2. Run Welch's t-test (equal_var=False) to test whether Treatment B yields a statistically significant increase.",
                    "3. Interpret t-statistic and p-value at alpha = 0.05."
                ]
            }
        ],
        "interpretation": "Mean A = 44.35, Mean B = 53.45. t-statistic = -7.95, p-value = 1.69e-09. Since p < 0.05, we reject the null hypothesis; Treatment Variant B demonstrates a statistically significant improvement."
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
                    "Load scikit-learn Diabetes dataset into DataFrame.",
                    "Compute Pearson correlation between 'bmi' and 'target' disease progression.",
                    "Fit OLS Simple Linear Regression: target = beta0 + beta1 * bmi using statsmodels (with sm.add_constant).",
                    "Interpret R-squared and p-value."
                ]
            },
            {
                "num": "Question 2: Multiple Linear Regression",
                "bullets": [
                    "Fit Multiple OLS model predicting 'target' using 'bmi', 'bp', and 'age'.",
                    "Evaluate model summary: R-squared, F-statistic, and individual feature p-values."
                ]
            },
            {
                "num": "Question 3: Spearman Rank Correlation",
                "bullets": [
                    "Given study_time = [2, 4, 1, 5, 3] and exam_score = [50, 65, 45, 80, 60].",
                    "Compute Spearman rank correlation coefficient and p-value using scipy.stats.",
                    "Interpret monotonic relationship."
                ]
            }
        ],
        "interpretation": "BMI alone explains 34.4% of variance (R2 = 0.344, p < 0.001). Adding BP and Age increases R2 to 39.6%, where BMI (p < 0.001) and BP (p < 0.001) are significant predictors, while Age (p = 0.685) is not. Study time and exam scores exhibit perfect rank correlation (rho = 1.0, p = 1.40e-24)."
    },
    {
        "id": "asm7",
        "title": "Practical 7",
        "topic": "Logistic Regression & Classification Metrics",
        "curl_da": "da.gd/s_asm7",
        "curl_is": "is.gd/sid_7",
        "questions": [
            {
                "num": "Question 1: Customer Churn Logistic Regression",
                "bullets": [
                    "Load 'scikit-learn/churn-prediction' dataset.",
                    "Predict binary 'Churn' (0=No, 1=Yes) using 'tenure' and 'MonthlyCharges'.",
                    "Train/test stratified split (80-20).",
                    "Evaluate with Confusion Matrix, Accuracy, Precision, Recall, F1-Score, and Classification Report.",
                    "Plot ROC Curve and compute AUC score."
                ]
            },
            {
                "num": "Question 2: Palmer Penguins Binary Classification Pipeline",
                "bullets": [
                    "Filter Palmer Penguins dataset for species 'Adelie' (0) and 'Gentoo' (1).",
                    "Features: bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g.",
                    "Build ML Pipeline with StandardScaler + LogisticRegression(max_iter=1000).",
                    "Evaluate model metrics and plot ROC curve with AUC."
                ]
            }
        ],
        "interpretation": "Churn prediction yields Accuracy = 77.4% with AUC = 0.810 (strong discriminatory ability). Palmer Penguins pipeline achieves perfect 100% accuracy (AUC = 1.00) because Adelie and Gentoo species are linearly separable across body mass and flipper length dimensions."
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
                    "Load Wine dataset (178 samples, 13 features).",
                    "Standardize features with StandardScaler.",
                    "Compute Explained Variance Ratio and Cumulative Explained Variance.",
                    "Identify minimum components required to retain >= 90% variance.",
                    "Transform data into 2 components and generate 2D scatter plot colored by wine class."
                ]
            },
            {
                "num": "Question 3: PCA on Breast Cancer Dataset",
                "bullets": [
                    "Load Breast Cancer dataset (569 observations, 30 features).",
                    "Standardize with StandardScaler and apply PCA.",
                    "Determine components explaining >= 90% variance.",
                    "Plot Cumulative Explained Variance curve (scree plot) with 90% variance threshold line."
                ]
            }
        ],
        "interpretation": "Wine dataset dimensionality is reduced from 13 features to 8 components while preserving 92.0% variance; 2D projection clearly separates the 3 wine classes. Breast Cancer dataset is reduced from 30 features down to 7 components retaining 91.0% variance."
    },
    {
        "id": "asm9",
        "title": "Practical 9",
        "topic": "Bayesian Updating for Medical Diagnostic Testing",
        "curl_da": "da.gd/s_asm9",
        "curl_is": "is.gd/sid_9",
        "questions": [
            {
                "num": "Question: Medical Diagnostic Testing with Bayes' Theorem",
                "bullets": [
                    "Prior disease prevalence: P(Disease) = 0.01 (1%).",
                    "Test Sensitivity: P(+ | Disease) = 0.95 (95%).",
                    "Test Specificity: P(- | No Disease) = 0.90 (90%) -> False Positive Rate = 0.10 (10%).",
                    "1. Compute total probability of a positive test: P(+).",
                    "2. Compute posterior probability of disease given a positive test: P(Disease | +).",
                    "3. Interpret in terms of the Base-Rate Fallacy."
                ]
            }
        ],
        "interpretation": "Total positive test probability P(+) = 10.85%. Despite 95% sensitivity, the posterior probability of actually having the disease given a positive test is only 8.76%! This illustrates the Base-Rate Fallacy: because the disease is rare (1%), false positives from the 99% healthy cohort outnumber true positives from the 1% sick cohort."
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
        Run any of these in a Jupyter cell to instantly copy that practical's full question and code into your clipboard (then press Ctrl + V to paste):
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

print("Regenerated asm.html with full questions and interpretation boxes! Size:", len(html_content))

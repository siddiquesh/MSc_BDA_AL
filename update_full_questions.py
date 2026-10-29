import os

root = r'c:\Users\asdf\Downloads\MSc_BDA_AL-'
asm_dir = os.path.join(root, 'asm')

questions = {
    1: '''"""
================================================================================
PRACTICAL 1: DESCRIPTIVE STATISTICS & EXPLORATORY DATA ANALYSIS (EDA)
================================================================================
FULL QUESTIONS:

Q1) Analyze the Iris Dataset:
    1. Load the Iris Dataset.
    2. Calculate mean of each numerical feature.
    3. Calculate median of each numerical feature.
    4. Calculate mode(s) of each numerical feature.
       (Note: Mode can be multi-modal or cannot be calculated for continuous data)
    5. Calculate standard deviation of each numerical feature.
    6. Calculate variance of each numerical feature.
    7. Calculate skewness of each numerical feature.
    8. Calculate kurtosis of each numerical feature.
    9. Plot the distribution (histogram with KDE) for each numerical feature.
    10. Interpret the results.

Q2) Analyze the Tips Dataset:
    1. Load the Tips Dataset.
    2. Calculate summary statistics (Mean, Median, Mode, Std Dev, Variance, Skewness, Kurtosis)
       for all numerical features (total_bill, tip, size).
    3. Plot histograms with KDE for numerical features.
    4. Interpret the results.

Q3) Analyze the Indian Stock Market Dataset:
    1. Load 'indian_stock_market.csv'.
    2. Calculate summary statistics (Mean, Median, Mode, Std Dev, Variance, Skewness, Kurtosis)
       for numerical stock prices (MSFT, IBM, SBUX, AAPL, GSPC).
    3. Plot distribution histograms with KDE.
    4. Interpret the results.
================================================================================
"""''',

    2: '''"""
================================================================================
PRACTICAL 2: PROBABILITY DISTRIBUTIONS (NORMAL, BINOMIAL, POISSON)
================================================================================
FULL QUESTIONS:

Q1) Normal Distribution:
    Plot a Normal Distribution with mean (mu) = 70 and standard deviation (sigma) = 10
    over the range x in [20, 120].
    Interpret: The curve is symmetric, centered at 70, and bell-shaped.

Q2) Effect of Standard Deviation on Normal Distribution:
    Fix mean mu = 70. Plot three normal curves with standard deviations sigma = 5, 10, 15.
    Interpret: 
    - sigma = 5 is the most concentrated/tallest.
    - sigma = 15 has the greatest spread/flattest.
    - As sigma increases, the peak height decreases and spread increases.

Q3) Effect of Mean on Normal Distribution:
    Fix standard deviation sigma = 10. Plot three normal curves with means mu = 50, 70, 90.
    Interpret:
    - When mean changes with constant sigma, the normal curve shifts horizontally
      along the x-axis. Its shape, spread, and height remain unchanged.

Q4) Binomial Distribution:
    Plot the Probability Mass Function (PMF) of a Binomial Distribution for n = 20 customers
    with probability of purchase p = 0.3.
    Interpret: Represents the discrete likelihood of different numbers of customer purchases.

Q5) Poisson Distribution:
    Plot the PMF of a Poisson Distribution with an average rate lambda = 4 calls per minute
    over x = 0 to 14.
    Interpret: Poisson is a discrete distribution where expected number of calls equals lambda = 4.
================================================================================
"""''',

    3: '''"""
================================================================================
PRACTICAL 3: CONFIDENCE INTERVALS & BOOTSTRAPPING
================================================================================
FULL QUESTIONS:

Question 1: (Parametric Student's t-based Confidence Interval)
    Given delivery times (in minutes) for 20 orders:
    [31, 28, 35, 42, 30, 27, 39, 33, 26, 32, 34, 31, 38, 26, 32, 41, 30, 36, 29, 37]
    1. Calculate the sample mean and sample standard deviation (ddof=1).
    2. Determine degrees of freedom (df = n - 1) and standard error (SE = s / sqrt(n)).
    3. Compute the 95% Confidence Interval for the population mean delivery time
       using the Student's t-distribution critical value.

Question 2: (Non-Parametric Bootstrap Confidence Interval)
    1. Estimate the 95% Confidence Interval for the mean delivery time using Bootstrapping
       with 5,000 resamples (sampling with replacement, random seed 42).
    2. Calculate the 2.5th and 97.5th percentiles of the bootstrap distribution.
    3. Compare the t-based CI and Bootstrap CI in terms of range and interval width.
================================================================================
"""''',

    4: '''"""
================================================================================
PRACTICAL 4: HYPOTHESIS TESTING (T-TEST, CHI-SQUARE, ONE-WAY ANOVA & TUKEY HSD)
================================================================================
FULL QUESTIONS:

Question 1: (Two-Sample Independent t-Test)
    Using the Titanic dataset, perform Welch's independent two-sample t-test
    (equal_var=False) to test if there is a statistically significant difference
    between ticket fares paid by male passengers vs female passengers.
    H0: Mean fare of male = Mean fare of female.

Question 2: (Chi-Square Test of Independence)
    Using the Titanic dataset, construct a contingency table crossing passenger
    'class' (First, Second, Third) with 'survived' status (0, 1).
    Perform a Chi-Square test of independence to assess whether passenger class
    is significantly associated with survival outcome.

Question 3: (One-Way ANOVA & Post-Hoc Tukey HSD Test)
    Test the hypothesis:
    H0: Mean ticket fares do not differ significantly across the 3 passenger classes
        (First, Second, Third).
    1. Perform One-Way ANOVA (f_oneway).
    2. If p < 0.05, perform Tukey's Honestly Significant Difference (HSD) test
       to identify which specific pairwise passenger classes differ in mean fare.
================================================================================
"""''',

    5: '''"""
================================================================================
PRACTICAL 5: A/B TESTING
================================================================================
FULL QUESTIONS:

Question: (A/B Testing Analysis with Two-Sample Welch's t-Test)
    Given conversion / performance metrics from an A/B test with 20 users per group:
    - Control Group A:
      [42, 38, 45, 51, 47, 39, 44, 50, 46, 41, 43, 48, 37, 49, 45, 40, 52, 44, 46, 43]
    - Treatment Variant Group B:
      [48, 52, 55, 49, 58, 51, 54, 56, 50, 53, 57, 49, 55, 52, 59, 54, 51, 56, 53, 55]

    1. Calculate the sample mean for Group A and Group B.
    2. Conduct an independent two-sample t-test (Welch's t-test, equal_var=False)
       to determine whether Group B exhibits a statistically significant improvement.
    3. Interpret the resulting t-statistic and p-value at alpha = 0.05.
================================================================================
"""''',

    6: '''"""
================================================================================
PRACTICAL 6: LINEAR REGRESSION & CORRELATION
================================================================================
FULL QUESTIONS:

Question 1: (Simple Linear Regression)
    Load the scikit-learn Diabetes dataset into a pandas DataFrame.
    1. Evaluate the Pearson correlation between Body Mass Index ('bmi') and the
       disease progression outcome ('target').
    2. Fit an Ordinary Least Squares (OLS) Simple Linear Regression model
       (target ~ bmi + intercept) using statsmodels.
    3. Output and interpret the model summary (R-squared, coefficients, p-values).

Question 2: (Multiple Linear Regression)
    Fit an OLS Multiple Linear Regression model predicting disease progression ('target')
    using three predictors: 'bmi', blood pressure ('bp'), and 'age'.
    Add an intercept constant and evaluate:
    - Overall model fit (R-squared, F-statistic).
    - Which individual variables are statistically significant predictors.

Question 3: (Spearman Rank Correlation)
    Given:
    study_time = [2, 4, 1, 5, 3]
    exam_score = [50, 65, 45, 80, 60]
    Calculate the Spearman rank correlation coefficient and p-value.
    Interpret the monotonic relationship between study time and exam score.
================================================================================
"""''',

    7: '''"""
================================================================================
PRACTICAL 7: LOGISTIC REGRESSION & CLASSIFICATION
================================================================================
FULL QUESTIONS:

Question 1: (Customer Churn Prediction with Logistic Regression)
    Load the customer churn prediction dataset ('scikit-learn/churn-prediction').
    1. Use 'tenure' and 'MonthlyCharges' as predictors to predict binary 'Churn' (No=0, Yes=1).
    2. Split data into training (80%) and testing (20%) sets using stratified sampling.
    3. Fit a Logistic Regression model on the training set.
    4. Predict on the test set and evaluate using:
       - Confusion Matrix
       - Accuracy, Precision, Recall, F1-Score
       - Classification Report
    5. Compute predicted probabilities, generate the ROC curve, and calculate the AUC score.

Question 2: (Binary Classification Pipeline on Palmer Penguins)
    Load the Palmer Penguins dataset and filter for species 'Adelie' and 'Gentoo'.
    1. Use four features: bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g.
    2. Encode target species: Adelie=0, Gentoo=1.
    3. Build a Machine Learning Pipeline consisting of:
       - StandardScaler()
       - LogisticRegression(max_iter=1000)
    4. Train on 80% train split and evaluate on 20% test split.
    5. Output Confusion Matrix, Accuracy, Precision, Recall, F1-Score,
       Classification Report, and ROC Curve with AUC score.
================================================================================
"""''',

    8: '''"""
================================================================================
PRACTICAL 8: PRINCIPAL COMPONENT ANALYSIS (PCA)
================================================================================
FULL QUESTIONS:

Question 1 & 2: (PCA on Wine Dataset)
    Load the scikit-learn Wine dataset (178 samples, 13 features).
    1. Standardize all 13 features using StandardScaler.
    2. Apply PCA and calculate the Explained Variance Ratio and Cumulative Explained Variance.
    3. Determine the minimum number of principal components required to retain
       at least 90% of the total variance.
    4. Transform the dataset using PCA with 2 components and plot a 2D scatter plot
       colored by wine class to visualize class separability.

Question 3: (PCA on Breast Cancer Dataset with Scree Plot)
    Load the scikit-learn Breast Cancer dataset (569 observations, 30 features).
    1. Standardize all 30 features using StandardScaler.
    2. Apply PCA and compute the cumulative explained variance.
    3. Find the minimum number of components explaining at least 90% variance.
    4. Plot the Cumulative Explained Variance curve (scree plot) with a red dashed
       line at 90% variance threshold.
================================================================================
"""''',

    9: '''"""
================================================================================
PRACTICAL 9: BAYESIAN UPDATING FOR MEDICAL DIAGNOSTIC TESTING
================================================================================
FULL QUESTIONS:

Question: (Bayes' Theorem in Medical Diagnostic Testing)
    A diagnostic test for a disease has the following epidemiological characteristics:
    - Prior probability of disease in the population: P(Disease) = 0.01 (1%)
    - Test Sensitivity (True Positive Rate): P(+ | Disease) = 0.95 (95%)
    - Test Specificity (True Negative Rate): P(- | No Disease) = 0.90 (90%)
    - False Positive Rate: P(+ | No Disease) = 1 - Specificity = 0.10 (10%)

    Using Bayes' Theorem:
    1. Calculate the total probability of a positive test:
       P(+) = P(+ | Disease) * P(Disease) + P(+ | No Disease) * P(No Disease)
    2. Calculate the posterior probability of disease given a positive test:
       P(Disease | +) = [P(+ | Disease) * P(Disease)] / P(+)
    3. Interpret the result in terms of the Base-Rate Fallacy.
================================================================================
"""'''
}

# 1. Update individual asm_1.py to asm_9.py
all_combined = ['"""\n' + '='*80 + '\nAPPLIED STATISTICAL METHODS (ASM) - PRACTICALS 1 TO 9\nFULL QUESTIONS & IMPLEMENTATION\n' + '='*80 + '\n"""\n']

for i in range(1, 10):
    src_path = os.path.join(asm_dir, f'asm_{i}.py')
    with open(src_path, 'r', encoding='utf-8') as f:
        existing = f.read()
    
    # Strip old header comment if any
    lines = existing.splitlines()
    code_start = 0
    for idx, l in enumerate(lines):
        if l.strip().startswith(('import ', 'from ', 'delivery_time', 'group_A', 'prior_disease', 'wine', 'mu =', 'sigma=')):
            code_start = idx
            break
    code_body = '\n'.join(lines[code_start:])
    
    full_content = questions[i] + '\n\n' + code_body
    
    # Save to asm/asm_{i}.py
    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    all_combined.append(f"\n# {'='*78}\n# ASM PRACTICAL {i}\n# {'='*78}\n" + full_content)
    print(f'Updated asm_{i}.py with full question')

# Save all_asm_practicals.py
all_asm_file = os.path.join(asm_dir, 'all_asm_practicals.py')
with open(all_asm_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(all_combined))
print('Updated all_asm_practicals.py with full questions')

# Copy to root files so curl delivers the full questions!
for i in range(1, 10):
    src = os.path.join(asm_dir, f'asm_{i}.py')
    for dst in [f'practical_{i}.py', f'p{i}.py', f'asm{i}.py', f'asm{i}', f'{i}']:
        with open(src, 'r', encoding='utf-8') as sf, open(os.path.join(root, dst), 'w', encoding='utf-8') as df:
            df.write(sf.read())
    if i == 2:
        for dst in ['practical_2a.py', 'practical_2b.py', 'p2a.py', 'p2b.py', '2b']:
            with open(src, 'r', encoding='utf-8') as sf, open(os.path.join(root, dst), 'w', encoding='utf-8') as df:
                df.write(sf.read())

for dst in ['all_practicals_1_to_6.py', 'all.py', 'all', 'asm_all.py', 'asmall', 'asm0']:
    with open(all_asm_file, 'r', encoding='utf-8') as sf, open(os.path.join(root, dst), 'w', encoding='utf-8') as df:
        df.write(sf.read())

print('Copied all updated files to root!')

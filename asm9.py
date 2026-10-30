"""
================================================================================
PRACTICAL 9: BAYESIAN UPDATING FOR MEDICAL DIAGNOSTIC TESTING
================================================================================
FULL QUESTIONS:

Question: (Sequential Bayesian Updating for Medical Diagnostic Testing)
    A diagnostic medical test has the following characteristics:
    - Prior probability of disease: P(Disease) = 0.01 (1%)
    - Test Sensitivity: P(+ | Disease) = 0.95 (95%)
    - Test Specificity: P(- | No Disease) = 0.90 (90%)
    - False Positive Rate: P(+ | No Disease) = 1 - Specificity = 0.10 (10%)

    1. Calculate total probability of a positive test: P(+).
    2. Compute the Posterior Probability after the FIRST positive test.
    3. Use the first posterior as the NEW PRIOR and compute the Posterior Probability
       after a SECOND independent positive test!
================================================================================
"""

# Bayesian Updating for Medical Testing

# Prior probability
prior_disease = 0.01

# Test characteristics
sensitivity = 0.95
specificity = 0.90
false_positive_rate = 1 - specificity

# Probability of a positive test among people without disease
prob_positive = (
    sensitivity * prior_disease + false_positive_rate * (1 - prior_disease)
)

posterior_1 = (
    sensitivity * prior_disease
) / prob_positive

print("Probability of a positive test:", prob_positive)
print("Posterior probability after first positive test:", posterior_1)

# ------------------------------------------------------------------------------
# Sequential Bayesian Updating (Second Positive Test)
# ------------------------------------------------------------------------------
# Use posterior probability after first test as new prior!
new_prior = posterior_1

prob_positive_2 = (
    sensitivity * new_prior + false_positive_rate * (1 - new_prior)
)

posterior_2 = (
    sensitivity * new_prior
) / prob_positive_2

print("
--- Summary of Sequential Bayesian Tests ---")
print("Posterior probability after FIRST positive test :", posterior_1)
print("Posterior probability after SECOND positive test:", posterior_2)

"""
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
"""

prior_disease = 0.01

# Test characteristics
sensitivity = 0.95
specificity = 0.90

# Probability of a positive test among people without disease
false_positive_rate = 1 - specificity

# Bayes' theorem after first positive test
prob_positive = (
    sensitivity * prior_disease +
    false_positive_rate * (1 - prior_disease)
)

# Posterior probability P(Disease | Positive)
posterior_disease = (sensitivity * prior_disease) / prob_positive

print("Prior Probability of Disease:", prior_disease)
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)
print("False Positive Rate:", false_positive_rate)
print("Probability of Positive Test:", prob_positive)
print("Posterior Probability of Disease given Positive Test:", posterior_disease)
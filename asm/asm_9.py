"""
================================================================================
PRACTICAL 9: BAYESIAN INFERENCE & SEQUENTIAL UPDATING
================================================================================
FULL QUESTIONS:

Sequential Bayesian Updating for Medical Testing:
A diagnostic test is used to detect a rare disease in a population.
- Disease prevalence (prior probability): P(Disease) = 0.01 (1%).
- Test sensitivity (True Positive Rate): P(+ | Disease) = 0.95 (95%).
- Test specificity (True Negative Rate): P(- | No Disease) = 0.90 (90%).
- False Positive Rate: P(+ | No Disease) = 1 - specificity = 0.10 (10%).

Tasks:
Q1) First Positive Test Update:
    - Calculate total probability of a positive test P(+).
    - Compute posterior probability of having the disease after one positive test:
      P(Disease | +).

Q2) Second Positive Test Update (Sequential Update):
    - Use the posterior probability from the first test as the new prior probability.
    - Calculate the new probability of a positive test.
    - Compute updated posterior probability of having the disease: P(Disease | +, +).
    - Provide diagnostic conclusion.
================================================================================
"""

# ------------------------------------------------------------------------------
# Q1: First Positive Test Update
# ------------------------------------------------------------------------------
# Prior probability
prior_disease = 0.01

# Test characteristics
sensitivity = 0.95
specificity = 0.90

# Probability of positive test among people without disease
false_positive_rate = 1 - specificity

# Bayes's theorem after first positive test
prob_positive = (sensitivity * prior_disease) + (false_positive_rate * (1 - prior_disease))

posterior_1 = (sensitivity * prior_disease) / prob_positive

print("--- Q1: First Positive Test ---")
print("probability of positive test: ", prob_positive)
print("posterior probability after first positive test: ", posterior_1)

# ------------------------------------------------------------------------------
# Q2: Sequential Update (Second Positive Test)
# ------------------------------------------------------------------------------
# Use the posterior probability after first test as the new prior
new_prior = posterior_1

prob_positive_2 = (sensitivity * new_prior) + (false_positive_rate * (1 - new_prior))

posterior_2 = (sensitivity * new_prior) / prob_positive_2

print("\n--- Q2: Second Positive Test (Sequential Update) ---")
print("probability of positive test: ", prob_positive_2)
print("posterior probability after second positive test: ", posterior_2)

"""
Conclusion:
If both tests are positive, there is a much higher chance of the user having the disease
(~48.06% compared to ~8.76% after one test, and 1% initial population baseline).
"""
# ASM Practical 9 - Bayesian Updating for Medical Testing

# Prior probability
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

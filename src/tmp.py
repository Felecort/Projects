from scipy.stats import chi2_contingency

observed =  ([10, 6], [ 5, 15])
print(chi2_contingency(observed))
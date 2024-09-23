import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr

# Data
BLEU = np.array([0.135, 0.175, 0.111, 0.393, 0.443, 0.225, 0.150, 0.179, 0.512, 0.258, 0.338])
HBLEU = np.array([0.213, 0.303, 0.260, 0.532, 0.572, 0.364, 0.238, 0.269, 0.634, 0.406, 0.475])
results_metric = np.array([0.00, 0.03, 0.00, 0.22, 0.25, 0.12, 0.04, 0.08, 0.59, 0.27, 0.29])

# Pearson correlation coefficients
pearson_corr_bleu = np.corrcoef(BLEU, results_metric)[0, 1]
pearson_corr_hbleu = np.corrcoef(HBLEU, results_metric)[0, 1]

# Spearman correlation coefficients
spearman_corr_bleu, _ = spearmanr(BLEU, results_metric)
spearman_corr_hbleu, _ = spearmanr(HBLEU, results_metric)

# Print correlation coefficients
print(f"Pearson Correlation with BLEU: {pearson_corr_bleu:.2f}")
print(f"Spearman Correlation with BLEU: {spearman_corr_bleu:.2f}")
print(f"Pearson Correlation with HybridBLEU: {pearson_corr_hbleu:.2f}")
print(f"Spearman Correlation with HybridBLEU: {spearman_corr_hbleu:.2f}")

# Plotting
plt.figure(figsize=(12, 6))

# Plot for BLEU
plt.subplot(1, 2, 1)
sns.regplot(x=BLEU, y=results_metric, ci=None, line_kws={"color": "red"})
plt.title(f'BLEU Score vs. Results-Based Metric\nPearson: {pearson_corr_bleu:.2f}, Spearman: {spearman_corr_bleu:.2f}')
plt.xlabel('BLEU')
plt.ylabel('Results-Based Metric')
plt.grid(True)

# Plot for HybridBLEU
plt.subplot(1, 2, 2)
sns.regplot(x=HBLEU, y=results_metric, ci=None, line_kws={"color": "red"})
plt.title(f'HybridBLEU vs. Results-Based Metric\nPearson: {pearson_corr_hbleu:.2f}, Spearman: {spearman_corr_hbleu:.2f}')
plt.xlabel('HybridBLEU')
plt.ylabel('Results-Based Metric')
plt.grid(True)

plt.tight_layout()
plt.show()

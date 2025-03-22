import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set a random seed for reproducibility
np.random.seed(42)

# Generate normally distributed data
n_samples = 1000
mean = 50
std_dev = 10

# Generate the main data following normal distribution
data = np.random.normal(mean, std_dev, n_samples)

# Add some outliers
outliers = np.array([mean + 4*std_dev, mean - 4*std_dev, 
                     mean + 5*std_dev, mean - 4.5*std_dev,
                     mean + 6*std_dev])
                     
# Combine the data
combined_data = np.concatenate([data, outliers])

# Create a DataFrame
df = pd.DataFrame({
    'values': combined_data,
    'is_outlier': [False] * n_samples + [True] * len(outliers)
})

print("DataFrame shape:", df.shape)
print("\nDataFrame head:")
print(df.head())
print("\nDataFrame statistics:")
print(df.describe())

# Method 1: Z-score method
def detect_outliers_zscore(data, threshold=3):
    z_scores = np.abs(stats.zscore(data))
    return z_scores > threshold

# Method 2: IQR method
def detect_outliers_iqr(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    return (data < lower_bound) | (data > upper_bound)

# Apply outlier detection methods
df['outlier_zscore'] = detect_outliers_zscore(df['values'])
df['outlier_iqr'] = detect_outliers_iqr(df['values'])

# Count detected outliers
print("\nOutliers detected with Z-score method:", df['outlier_zscore'].sum())
print("Outliers detected with IQR method:", df['outlier_iqr'].sum())

# Check which actual outliers were detected by each method
print("\nZ-score method detection accuracy:")
print(pd.crosstab(df['is_outlier'], df['outlier_zscore'], 
                 rownames=['Actual'], colnames=['Predicted']))
print("\nIQR method detection accuracy:")
print(pd.crosstab(df['is_outlier'], df['outlier_iqr'], 
                 rownames=['Actual'], colnames=['Predicted']))

# Visualize the data and detected outliers
plt.figure(figsize=(15, 6))

# Plot 1: Distribution with actual outliers
plt.subplot(1, 3, 1)
sns.histplot(df['values'], kde=True)
plt.title('Data Distribution')
plt.xlabel('Values')
actual_outliers = df[df['is_outlier']]['values']
for value in actual_outliers:
    plt.axvline(x=value, color='red', linestyle='--', alpha=0.7)
plt.text(0.05, 0.95, f"Actual outliers: {len(actual_outliers)}", 
         transform=plt.gca().transAxes, fontsize=10,
         bbox=dict(facecolor='white', alpha=0.5))


plt.subplot(1, 3, 2)
sns.histplot(df['values'], kde=True)
plt.title('Z-score Outlier Detection')
plt.xlabel('Values')
zscore_outliers = df[df['outlier_zscore']]['values']
for value in zscore_outliers:
    plt.axvline(x=value, color='orange', linestyle='--', alpha=0.7)
plt.text(0.05, 0.95, f"Z-score outliers: {len(zscore_outliers)}", 
         transform=plt.gca().transAxes, fontsize=10,
         bbox=dict(facecolor='white', alpha=0.5))

plt.subplot(1, 3, 3)
sns.histplot(df['values'], kde=True)
plt.title('IQR Outlier Detection')
plt.xlabel('Values')
iqr_outliers = df[df['outlier_iqr']]['values']
for value in iqr_outliers:
    plt.axvline(x=value, color='green', linestyle='--', alpha=0.7)
plt.text(0.05, 0.95, f"IQR outliers: {len(iqr_outliers)}", 
         transform=plt.gca().transAxes, fontsize=10,
         bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x=df['values'])
plt.title('Box Plot of Data with Outliers')
plt.xlabel('Values')
plt.tight_layout()
plt.show()

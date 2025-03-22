import pandas as pd
import numpy as np

data = {
    'ID': [1, 2, 3, 4, 5, 5, 6, np.nan],
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eve', 'Eve', 'Frank', 'Grace'],
    'Age': [25, np.nan, 30, 22, np.nan, 35, 40, 28],
    'Salary': [50000, 60000, np.nan, 45000, 70000, 70000, np.nan, 55000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 1. Identifying missing data
print("\nIdentifying missing values:")
print(df.isna())  # Shows True for missing values
print("\nCount of missing values in each column:")
print(df.isna().sum())

# 2. Filtering out missing data using dropna
print("\nDropping rows with any missing values:")
df_dropped = df.dropna()
print(df_dropped)

print("\nDropping rows with all missing values:")
df_dropped_all = df.dropna(how='all')
print(df_dropped_all)

print("\nDropping rows with missing values in specific columns:")
df_dropped_subset = df.dropna(subset=['Name', 'Age'])
print(df_dropped_subset)

# 3. Filling missing data using fillna
print("\nFilling missing values with specific values:")
df_filled = df.fillna({'Age': df['Age'].mean(), 'Salary': df['Salary'].mean(), 'ID': 0})
print(df_filled)

print("\nFilling using forward fill method:")
df_ffill = df.fillna(method='ffill')
print(df_ffill)

print("\nFilling using backward fill method:")
df_bfill = df.fillna(method='bfill')
print(df_bfill)

# 4. Removing duplicates
print("\nIdentifying duplicate rows:")
print(df.duplicated())

print("\nRemoving duplicate rows (keeping first):")
df_no_dupes = df.drop_duplicates()
print(df_no_dupes)

print("\nRemoving duplicates based on specific columns:")
df_no_dupes_subset = df.drop_duplicates(subset=['Name', 'Age'])
print(df_no_dupes_subset)


df_cleaned = df.fillna({'Age': df['Age'].mean(), 'Salary': df['Salary'].mean(), 'ID': 0}).drop_duplicates()
print("\nFinal cleaned DataFrame:")
print(df_cleaned)

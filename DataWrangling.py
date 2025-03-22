import pandas as pd
import numpy as np


print("Part a: Hierarchical Indexing and Partial Indexing")
print("-" * 50)


hierarchical_index = [['East', 'East', 'East', 'West', 'West', 'West'],
                     ['NY', 'MA', 'FL', 'CA', 'OR', 'WA']]


data = [320, 180, 410, 560, 210, 320]


sales = pd.Series(data, index=hierarchical_index)
print("Original Series with hierarchical index:")
print(sales)
print()


sales.index = pd.MultiIndex.from_arrays(hierarchical_index, names=['Region', 'State'])
print("Series with named MultiIndex:")
print(sales)
print()

print("Subset of data for 'East' region:")
print(sales['East'])
print()

print("Subset of data for 'West' region:")
print(sales['West'])
print()

print("Selecting specific state 'NY' from 'East' region:")
print(sales['East', 'NY'])
print()

print("Selecting multiple states using .loc:")
print(sales.loc[['East', 'West'], ['MA', 'CA']])
print()


print("\nPart b: Rearranging Data with stack() and unstack()")
print("-" * 50)


index = pd.MultiIndex.from_product([['East', 'West'], ['NY', 'MA', 'FL', 'CA', 'OR', 'WA']], 
                                 names=['Region', 'State'])
columns = pd.MultiIndex.from_product([['Q1', 'Q2'], ['Electronics', 'Clothing']], 
                                    names=['Quarter', 'Category'])

# Generate some random data
np.random.seed(42)  
data = np.round(np.random.rand(12, 4) * 1000)
df = pd.DataFrame(data, index=index, columns=columns)

print("Original DataFrame with hierarchical index and columns:")
print(df)
print()

print("Unstacking the 'State' level (inner index):")
unstacked = df.unstack(level='State')
print(unstacked)
print()

print("Stacking the 'Category' level (inner column):")
stacked = df.stack(level='Category')
print(stacked)
print()

print("Unstacking 'Region' then stacking 'Quarter':")
transformed = df.unstack('Region').stack('Quarter')
print(transformed)
print()


print("Swapping index levels:")
swapped = sales.swaplevel()
print(swapped)
print("Notice that the State is now the outer index level")

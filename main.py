import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Dubai_Property_Analysis/properties_data.csv")

# To display the first few rows, you need to call head() as a method and print it
print("DataFrame Head:")
print(df.head())

# FIX 1: Corrected .reset.index() to .reset_index()
avg_price_by_quality = df.groupby("quality")["price"].mean().reset_index()

avg_price_by_quality.columns = ['Quality', 'Average Price']

print("\nAverage Price by Quality:")
print(avg_price_by_quality)

# FIX 2: Use the correct variable name 'avg_price_by_quality'
quality_order = avg_price_by_quality['Quality'].tolist() # Use the correct variable name
average_prices = avg_price_by_quality['Average Price'].tolist() # Use the correct variable name

# Now you can use these lists to plot
plt.figure(figsize=(10, 6))
plt.bar(quality_order, average_prices, color='skyblue')
plt.title('Average Property Price by Quality in Dubai')
plt.xlabel('Quality')
plt.ylabel('Average Price (AED)')
plt.show()

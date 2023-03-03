import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Final_Assignment_SQLRDY.csv")
# Most popular item based on zip code
most_popular_item = df.groupby(['zip_code', 'item_description']).sum().sort_values('bottles_sold', ascending=False)
# Percentage of sales
total_sales = df['sale_dollars'].sum()
sales_by_store = df.groupby(['store_number']).sum()
percentage = sales_by_store / total_sales
# Scatter plot
plt.scatter(df['zip_code'], df['bottles_sold'], color=np.random.rand(3, ))
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Total Bottles Sold')
plt.show()

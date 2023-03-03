# FinalAssignment
For MySQL a new connection was created
1. The dataset that was provided (finance_liquor_sales.sql) was added to the Workbench in MySQL.
2. To select all the columns of the table between the year 2016-2019 the following querries were used:
use liquorsales;
show tables;
select * from finance_liquor_sales
where date(date) between '2016-01-01' and '2020-01-01';

3. Finally the newly made file was exproted through MySQL as a CSV file

Python 3 code was executed in an integrated development environment called PyCharm


4. To get the most popular item sold based on zip code the following code was used:

import pandas as pd

df = pd.read_csv("Final_Assignment_SQLRDY.csv")

most_popular_item = df.groupby(['zip_code', 'item_description']).sum().sort_values('bottles_sold', ascending=False)
print(most_popular_item.head())

To get the percentage of sales per store the following code was used:

import pandas as pd

df = pd.read_csv("Final_Assignment_SQLRDY.csv")

total_sales = df['sale_dollars'].sum()
sales_by_store = df.groupby(['store_number']).sum()
percentage = sales_by_store/total_sales
print(percentage)

5. To create a scatter plot the Matplotlib library was imported and the following code was used:

import matplotlib.pyplot as plt
impoert pandas as pd
import numpy as np

df = pd.read_csv("Final_Assignment_SQLRDY.csv")

plt.scatter(df['zip_code'], df['bottles_sold'], color=np.random.rand(3,))
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Total Bottles Sold')
plt.show()

** color can be anything, in this code we use numpy to give a random color everytime.

Final Thoughts
Finding the most popular item based on zip code was difficult. At first my code was:
most_popular_item = df.groupby(['zip_code', 'bottles_sold']).sort_values.sum('bottles_sold', ascending=False)
and as you can imagine i did not work properly. After some help and a lot of search i spotted my mistakes. 

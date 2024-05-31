'''15.3Write a Pandas program to create a stacked histograms plot of
opening, closing, high, low stock prices of Alphabet Inc. between
two specific dates.'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')                         
df['Date'] = pd.to_datetime(df['Date']) 
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Open','Close','High','Low']]
plt.figure(figsize=(25,25))
df2.plot.hist(stacked=True, bins=20)
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc.,\n From 01-04-2020 to 30-09-2020', fontsize=12, color='blue')
plt.show()

#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import yfinance as yf

### PART 1 ###
atom_wts = [1, 4, 7, 9, 11, 12]
elems = ['H', 'He', 'Li', 'Be', 'B', 'C']


plt.pie(atom_wts, labels=elems, autopct='%.1f%%', explode=[0,0.2,0,0,0,0])
plt.title('Percentage Pie Chart')
plt.show()

wedges, texts, autotexts = plt.pie(atom_wts, labels=elems, autopct='', explode=[0,0,0,0,0,0.1])

# Set the auto percentage text to the atomic weight
for i, text in enumerate(autotexts):
    text.set_text(f"{atom_wts[i]}")

plt.title('Atomic Weight Pie Chart')
plt.show()

### PART 2 ###
df = pd.read_csv('py_ide2.csv')
df.plot.bar(x='IDE', y='Adoption', title='IDE Adoption Rate', xlabel='IDE',
            ylabel='Adoption', rot=45, legend=False)
plt.tight_layout()
plt.show()

df.plot.barh(x='IDE', y='Adoption', title='IDE Adoption Rate', xlabel='Adoption',
            ylabel='IDE', legend=False)
plt.tight_layout()
plt.show()

### PART 3 ###
# First day of the month for 8 months
dates = ['01/01/2023','02/01/2023','03/01/2023','04/01/2023',
         '05/01/2023','06/01/2023','07/01/2023','08/01/2023']

# Random floats from 100 to 200
floats = np.random.uniform(low=100, high=200, size=8)

# Build DataFrame
df = pd.DataFrame({'Days': dates, 'Floats': floats})

# Convert days to datetime and set as index
df['Days'] = pd.to_datetime(df.Days, format='%m/%d/%Y')
df.set_index('Days')

fig, axs = plt.subplots(ncols=2, figsize=(12, 8))
df.plot(x='Days', y='Floats', ax=axs[0], legend=False)
df.plot.bar(x='Days', y='Floats', ax=axs[1], legend=False)
axs[1].set_xticklabels([d.strftime('%Y-%b') for d in df.Days], rotation=45)
plt.suptitle('Part 3 Plot')
plt.tight_layout()
plt.show()

### PART 4 ###
amzn = yf.Ticker('AMZN')
df = amzn.history()

fig, (price, vol) = plt.subplots(nrows=2, sharex=True)
df.plot(use_index=True, y='Close', ax=price, ylabel='Price', legend=False)
df.plot(use_index=True, y='Volume', ax=vol, ylabel='Volume', legend=False,
        color='r')
fig.suptitle('Amazon Stock Price and Volume')
plt.tight_layout()
plt.show()

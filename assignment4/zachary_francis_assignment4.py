#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import geoplot

df_states = gpd.read_file('states_geo.json')
df_data = pd.read_csv('SturmData.csv')

states = df_states[~df_states.name.str.contains('Alaska|Hawaii|District of Columbia|Puerto Rico')]
states['id'] = states.id.astype('int64')
states_data = states.merge(df_data, left_on='id', right_on='fips')

plots = list(df_data.columns[3:])
titles = [
    "Right to have Property Protected from Husband's Debt",
    "Right for Control of their Separate Property",
    "Right to Ownership of Wages and Earnings",
    "Right to Create Wills without Husband's Consent",
    "Right to Sign Contracts without Husband's Consent"
]
for i, plot in enumerate(plots):
    fig, ax = plt.subplots(figsize=(14,8))
    states_data.plot(column=plot, legend=True, edgecolor='black',
                     legend_kwds={'label': 'Year the Right was Granted',
                                  'orientation': 'horizontal'},
                     missing_kwds={'color': 'lightgrey',
                                   'edgecolor': 'black',
                                   'hatch': '///',
                                   'label': 'Missing'},
                     ax=ax, cmap='winter_r')
    ax.set_axis_off()
    fig.suptitle("Womens Suffrage By State", fontsize='x-large', fontweight='bold')
    ax.set_title(titles[i])
    plt.show()

#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt

### PART 1 ###
mpg = sns.load_dataset('mpg')
numeric_cols = mpg.columns[:7]
fig = plt.figure(figsize=(10,8))
ax1 = sns.heatmap(mpg[numeric_cols].corr())
ax1.set_title('Heatmap')
plt.yticks(rotation='horizontal')
plt.tight_layout()
plt.show()

ax2 = sns.pairplot(mpg[numeric_cols])
plt.tight_layout()
plt.show()

### PART 2 ###
diamonds = sns.load_dataset('diamonds')
diamonds = diamonds[~diamonds.color.isin(['D','E'])]
diamonds['color'] = diamonds.color.cat.remove_unused_categories()
diamonds = diamonds[diamonds.cut != "Fair"]
diamonds['cut'] = diamonds.cut.cat.remove_unused_categories()

grid = sns.FacetGrid(diamonds, col='color', row='cut', height=2.5, aspect=1.2)
grid.map(sns.scatterplot, 'carat', 'price')
plt.show()

### PART 3 ###
crashes = sns.load_dataset('car_crashes')

fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(10,5))
sns.regplot(data=crashes, x='speeding', y='total', ax=axs[0])
sns.regplot(data=crashes, x='alcohol', y='total', ax=axs[1])
axs[0].set_title('Speeding RegPlot')
axs[1].set_title('Alcohol RegPlot')
plt.suptitle('Relationship of Speeding and Alcohol to Total Crashes')
plt.show()

### PART 4 ###
iris = sns.load_dataset('iris')

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10,8))
cols = iris.columns[:4]
x_labels = [' '.join(label.split('_')).title() for label in cols]
for i, ax in enumerate(fig.axes):
    legend = True if i == 1 else False
    sns.histplot(data=iris, x=cols[i], hue='species', ax=ax, legend=legend,
                 multiple='stack')
    ax.set_xlabel(x_labels[i])
plt.suptitle('Distribution of Iris Attributes by Species')
plt.show()

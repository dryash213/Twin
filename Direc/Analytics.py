# 1837186
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
## Display all the columns of the dataframe

df = pd.read_csv("Fitabase Data 4.12.16-5.12.16\dailyActivity_merged.csv")

# print(df['TotalSteps'].describe())
plt.figure(figsize=(9, 8))
sns.distplot(df['Calories'], color='g', bins=100, hist_kws={'alpha': 0.4});
plt.savefig('fig1.png')

df.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8); # ; avoid having the matplotlib verbose informations
plt.savefig('fig2.png')

for i in range(0, len(df.columns), 5):
    sns.pairplot(data=df,
                x_vars=df.columns[i:i+5],
                y_vars=['Calories'])

plt.savefig('fig3.png')

corr = df.corr() # We already examined SalePrice correlations
plt.figure(figsize=(12, 10))

sns.heatmap(corr[(corr >= 0.5) | (corr <= -0.4)], 
            cmap='viridis', vmax=1.0, vmin=-1.0, linewidths=0.1,
            annot=True, annot_kws={"size": 8}, square=True);

plt.savefig('fig4.png')

features_to_analyse =[ 'TotalSteps', 'TotalDistance', 'TrackerDistance',
       'LoggedActivitiesDistance', 'VeryActiveDistance',
       'ModeratelyActiveDistance', 'LightActiveDistance',
       'SedentaryActiveDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes',
       'LightlyActiveMinutes', 'SedentaryMinutes', 'Calories']


fig, ax = plt.subplots(round(len(features_to_analyse) / 3), 3, figsize = (18, 12))

for i, ax in enumerate(fig.axes):
    if i < len(features_to_analyse) - 1:
        sns.regplot(x=features_to_analyse[i],y='Calories', data=df[features_to_analyse],color='orange', ax=ax)
plt.savefig('fig5.png')

sns.scatterplot('TotalSteps', 'Calories', data=df)
plt.savefig('fig6.png')
plt.show()


import sys

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data_file = sys.argv[1]
df = pd.read_csv(data_file, sep=",")

# Correlation matrix 
# heatmap = df.corr()
# top_feat = heatmap.index
# plt.figure(figsize=(10, 10))

# sns.set(style="white")
# cmap = sns.diverging_palette(220, 10, as_cmap=True)
# p = sns.heatmap(df[top_feat].corr(), annot=True, cmap=cmap)
# p.set_yticklabels(p.get_yticklabels(), rotation=35)
# p.set_xticklabels(p.get_xticklabels(), rotation=35)
# plt.show()

# Scatter plot (needs two numerical columns) to detect relations

# plt.scatter(df["PURCHASEPRICE"][:100], df["SALEPRICE"][:100])
# plt.title("Purchase price vs sale price")
# plt.xlabel("purchase price")
# plt.ylabel("sale price")
# plt.show()

print(df['SALEPRICE'].value_counts())
# df.boxplot(column=["SALEPRICE"], grid='True')
sns.boxplot(y=df['PURCHASEPRICE'])
plt.show()

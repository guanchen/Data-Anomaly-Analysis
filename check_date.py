import sys

import pandas as pd

customer_file = sys.argv[1]
customer_dataframe = pd.read_csv(customer_file, sep="|")

item_file = sys.argv[2]
item_dataframe = pd.read_csv(item_file, sep="|")

transaction_file = sys.argv[3]
transaction_dataframe = pd.read_csv(transaction_file, sep="|", low_memory=False)

# unique_dates = transaction_dataframe['DELIVERYDATE'].unique()
# sorted_unique_dates = sorted(unique_dates)
# print(sorted_unique_dates)

unique_dates = transaction_dataframe['SHIPDAYS'].unique()
sorted_unique_dates = sorted(unique_dates)
print(sorted_unique_dates)

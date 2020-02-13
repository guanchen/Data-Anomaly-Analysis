import argparse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def check_strctured_data_validity(dataframe, column_name, valid_length, min_valid_range, max_valid_range):
    """
    Function can be used to check structured data (e.g., dates, quantities) 
    """
    print(f"----------- {column_name} -----------")
    dataframe[column_name] = dataframe[column_name].fillna(value=0)
    min_value = dataframe[column_name].min()
    max_value = dataframe[column_name].max()

    if min_value < min_valid_range or min_value > max_valid_range:
        print(f"Range error based on minimum")
    elif max_value < min_valid_range or max_value > max_valid_range:
        print(f"Range error based on maximum")
    else:
        print(f"Didn't find any range error")

    print(f"----------- {column_name} -----------")
    length_no_valid_dataframe = dataframe[dataframe[column_name].map(str).apply(len) != valid_length]
    if len(length_no_valid_dataframe) > 0:
        length_no_valid_items = length_no_valid_dataframe[column_name]
        print(f"Length error: {length_no_valid_items}")
    else:
        print(f"Didn't find any length error")


def check_text_data_validity(dataframe, column_name, valid_range_list):
    print(f"----------- {column_name} -----------")
    unique_values = dataframe[column_name].unique()
    valid = True
    for unique in unique_values:
        if unique == np.nan or str(unique).strip() == "": continue
        if unique not in valid_range_list:
            print(f"value {unique} is not in valid range.")
            valid = False
    if valid:
        print(f"Didn't find any error")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--customers", help='CustomerDB')
    parser.add_argument("--items", help='ItemDB')
    parser.add_argument("--transactions", help='TransactionsDB')
    parser.add_argument("--sep", help='Separator', default='|')

    args = parser.parse_args()

    if args.customers:
        data_file = args.customers
        customer_dataframe = pd.read_csv(data_file, sep=args.sep)

        check_strctured_data_validity(customer_dataframe,  "USERID", 5, 10000, 50000)
        check_text_data_validity(customer_dataframe, "GENDER", ['M', 'F', 'N'])

    if args.items:
        data_file = args.items
        item_dataframe = pd.read_csv(data_file, sep=args.sep)    
        check_strctured_data_validity(item_dataframe, "ITEM", 6, 100000, 500000)

    if args.transactions:
        data_file = args.transactions
        transaction_dataframe = pd.read_csv(data_file, sep=args.sep)
        check_strctured_data_validity(transaction_dataframe, "USERID", 5, 10000, 50000)
        check_strctured_data_validity(transaction_dataframe, "ITEM", 6, 100000, 500000)
        check_text_data_validity(transaction_dataframe, "REVIEW", ['YES', 'NO'])
        # timestamp_freq = transaction_dataframe['TIMESTAMP'].value_counts()
        # fig, ax = plt.subplots()
        # timestamp_freq.plot(ax=ax, kind='bar')
        # plt.show()


# Define what to do if file is run as script
if __name__ == "__main__":
    main()

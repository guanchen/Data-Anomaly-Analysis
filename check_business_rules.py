import argparse

import pandas as pd


def compare_price(data_dataframe, column1, column2):
    """
    function to compare PURCHASEPRICE and SALEPRICE
    """
    # Check column1 > column2
    abnormal_dataframe = data_dataframe[data_dataframe[column1] > data_dataframe[column2]]
    print(f"{abnormal_dataframe.shape[0]} rows have {column1} > {column2}") 
    print("For example, ...")
    print(abnormal_dataframe.head(5))

    # Check both columns are 0
    abnormal_zero_dataframe = data_dataframe[
        (data_dataframe[column1] == 0)
        & (data_dataframe[column2] == 0)
    ]
    if abnormal_zero_dataframe.empty:
        print(f"Didn't find any row where both {column1} and {column2} are equal to 0")
    else:
        print(f"Find rows where both {column1} and {column2} are equal to 0")
        print(abnormal_zero_dataframe.head(5))

    # Check only one column is 0
    abnormal_zerocol1_dataframe = data_dataframe[data_dataframe[column1] == 0]
    if abnormal_zerocol1_dataframe.empty:
        print(f"Didn't find 0 value in {column1}")
    else:
        print(f"0 values in {column1} ({abnormal_zerocol1_dataframe.shape[0]}).")
        print(abnormal_zerocol1_dataframe.head(5))

    abnormal_zerocol2_dataframe = data_dataframe[data_dataframe[column2] == 0]
    if abnormal_zerocol2_dataframe.empty:
        print(f"Didn't find 0 value in {column2}")
    else:
        print(f" 0 values in {column2} ({abnormal_zerocol2_dataframe.shape[0]} rows).")
        print(abnormal_zerocol2_dataframe.head(5))





def main():
    parser = argparse.ArgumentParser()

    # Mandatory arguments
    parser.add_argument("data", help='Data file')

    # Optional arguments
    parser.add_argument("--column1", help='column name')
    parser.add_argument("--column2", help='another column name')
    parser.add_argument("--sep", help='Separator', default='|')

    args = parser.parse_args()

    data_file = args.data
    data_dataframe = pd.read_csv(data_file, sep=args.sep)

    if args.column1 and args.column2:
        compare_price(data_dataframe, args.column1, args.column2)


# Define what to do if file is run as script
if __name__ == "__main__":
    main()

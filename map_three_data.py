import argparse

import pandas as pd


def main():
    parser = argparse.ArgumentParser()

    # Mandatory arguments
    parser.add_argument("data1", help='Data file 1 to merge')
    parser.add_argument("data2", help='Data file 2 to merge')
    parser.add_argument("data3", help='Data file 3 to merge linking 1 and 2')
    parser.add_argument("column13", help='Column linking data 1 and 3')
    parser.add_argument("column32", help='Column linking data 2 and 3')

    # Optional arguments
    parser.add_argument("--output", help='CSV file output')
    parser.add_argument("--sep", help='Separator', default=',')
    args = parser.parse_args()

    data1_df = pd.read_csv(args.data1, sep=args.sep)
    data2_df = pd.read_csv(args.data2, sep=args.sep)
    data3_df = pd.read_csv(args.data3, sep=args.sep)

    data3_df[args.column13].dropna()
    data3_df[args.column32].dropna()

    customer_transaction_df = pd.merge(data1_df, data3_df, on=args.column13, how='inner')
    print(f"Before concatenating, the customer and transaction together have {data1_df.shape[0] + data2_df.shape[0]} rows.")
    print(f"After concatenating, the output has {customer_transaction_df.shape[0]} rows.")

    customer_transaction_item_df = pd.merge(customer_transaction_df, data2_df, on=args.column32, how="inner")
    print(f"Before concatenating, the customer_transaction_df and item_df together have {customer_transaction_df.shape[0] + data2_df.shape[0]} rows.")
    print(f"After concatenating, the output has {customer_transaction_item_df.shape[0]} rows.")

    if args.output:
        filename = args.output
    else:
        filename = "mapped_data.csv"

    customer_transaction_item_df.to_csv(filename, index=False)


# Define what to do if file is run as script
if __name__ == "__main__":
    main()

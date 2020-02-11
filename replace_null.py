import argparse

import pandas as pd


def replace_null_by_values(dataframe, values):
    value = values[0]
    null_dict = {}
    for column in dataframe.columns:
        null_dict.update({column: value})
    dataframe = dataframe.fillna(null_dict)

    return dataframe


def replace_null_by_columns_values(dataframe, columns, values):
    null_dict = {}

    if len(columns) == len(values):
        lenght = len(columns)
        for i in range(lenght):
            column = columns[i]
            value = values[i]
            null_dict.update({column: value})
    else:
        value = values[0]
        for column in columns:
            null_dict.update({column: value})

    dataframe = dataframe.fillna(null_dict)

    return dataframe


def replace_null_by_avg(dataframe, columns):

    null_dict = {}
    for column in columns:
        dataframe[column] = pd.to_numeric(dataframe[column], errors='coerce')
        value = dataframe[column].mean()
        null_dict.update({column: value})
        print(f"mean of {column}: {value}")
    dataframe = dataframe.fillna(null_dict)

    return dataframe


def main():
    parser = argparse.ArgumentParser()
    # Mandatory arguments
    parser.add_argument("data", help='Data file')
    # Optional arguments
    parser.add_argument(
        "-c",
        "--columns",
        nargs='+',
        help='Column(s) to replace [-c Column1 Column2]'
    )
    parser.add_argument("--output", help='CSV file output')
    parser.add_argument("--sep", help='Separator', default='|')
    parser.add_argument(
        "-v",
        "--values",
        nargs='+',
        help='Replace with the new value(s) [-v valueForC1 valueForC2]'
    )
    parser.add_argument("--avg", help="Average", action="store_true")
    args = parser.parse_args()

    data_file = args.data
    data_dataframe = pd.read_csv(data_file, sep=args.sep)

    # Check optionnal arguments
    if args.columns and args.avg:
        new_dataframe = replace_null_by_avg(data_dataframe, args.columns)

    if not args.columns and args.values:
        if len(args.values) != 1:
            print("Too many values")
            exit()
        else:
            new_dataframe = replace_null_by_values(
                                data_dataframe, args.values)

    if args.columns and args.values:
        if len(args.columns) != len(args.values) and len(args.values) != 1:
            print("Too many values")
            exit()
        else:
            new_dataframe = replace_null_by_columns_values(
                                data_dataframe, args.columns,
                                args.values)

    # if not args.values:
    #     print("No action done as no replacement value has been defined.")
    #     exit()

    print(new_dataframe)

    if args.output:
        filename = args.output
    else:
        filename = f"{data_file.split('.')[0]}_replaced_null.csv"

    new_dataframe.to_csv(filename, index=False)


# Define what to do if file is run as script
if __name__ == "__main__":
    main()

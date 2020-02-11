import argparse

import numpy
import pandas as pd


def replace_empty(dataframe):
    for column in dataframe.columns:
        try:
            dataframe.loc[
                dataframe[column].str.strip().str.len() == 0,
                column
            ] = numpy.nan
        except AttributeError:
            pass

    return dataframe


def replace_empty_by_columns(dataframe, columns):
    for column in columns:
        try:
            dataframe.loc[
                dataframe[column].str.strip().str.len() == 0,
                column
            ] = numpy.nan
        except AttributeError:
            pass

    return dataframe


def replace_empty_by_avg(dataframe, columns):
    for column in columns:
        try:
            dataframe[column] = pd.to_numeric(dataframe[column], errors='coerce')
            dataframe.loc[
                dataframe[column].str.strip().str.len() == 0,
                column
            ] = dataframe[column].mean()
        except AttributeError:
            pass

    return dataframe


def replace_empty_by_values(dataframe, values):
    value = values[0]
    for column in dataframe.columns:
        try:
            dataframe.loc[
                dataframe[column].str.strip().str.len() == 0,
                column
            ] = value
        except AttributeError:
            pass

    return dataframe


def replace_empty_by_columns_values(dataframe, columns, values):
    if len(columns) == len(values):
        lenght = len(columns)
        for i in range(lenght):
            column = columns[i]
            value = values[i]
            try:
                dataframe.loc[
                    dataframe[column].str.strip().str.len() == 0,
                    column
                ] = value
            except AttributeError:
                pass
    else:
        value = values[0]
        for column in columns:
            try:
                dataframe.loc[
                    dataframe[column].str.strip().str.len() == 0,
                    column
                ] = value
            except AttributeError:
                pass

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
    parser.add_argument("--avg", help="Average", action='store_true')
    parser.add_argument("--output", help='CSV file output')
    parser.add_argument("--sep", help='Separator', default='|')
    parser.add_argument(
        "-v",
        "--values",
        nargs='+',
        help='Replace with the new value(s) [-v valueForC1 valueForC2]'
    )
    args = parser.parse_args()

    data_file = args.data
    data_dataframe = pd.read_csv(data_file, sep=args.sep)

    # Check optionnal arguments
    if not args.columns and not args.values:
        new_dataframe = replace_empty(data_dataframe)

    if args.columns and not args.values:
        new_dataframe = replace_empty_by_columns(data_dataframe, args.columns)

    if not args.columns and args.values:
        if len(args.values) != 1:
            print("Too many values")
            exit()
        else:
            new_dataframe = replace_empty_by_values(
                                data_dataframe, args.values)

    if args.columns and args.values:
        if len(args.columns) != len(args.values) and len(args.values) != 1:
            print("Too many values")
            exit()
        else:
            new_dataframe = replace_empty_by_columns_values(
                                data_dataframe, args.columns,
                                args.values)
    if args.columns and args.avg:
        new_dataframe = replace_empty_by_avg(data_dataframe, args.columns)

    print(new_dataframe)

    if args.output:
        filename = args.output
    else:
        filename = f"{data_file.split('.')[0]}_replaced_empty.csv"

    # new_dataframe.to_csv(filename, index=False)


# Define what to do if file is run as script
if __name__ == "__main__":
    main()

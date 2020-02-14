import argparse

import pandas as pd


def remove_empty(dataframe):
    print("\n")
    print("----- DELETING EMPTY ENTRIES -----")

    string_dataframe = dataframe.applymap(str)
    no_space_df = string_dataframe.applymap(str.strip)
    no_empty_boolean_df = no_space_df.ne("")
    no_empty_entries = no_empty_boolean_df.all(axis='columns')
    new_dataframe = dataframe[no_empty_entries]

    return new_dataframe


def remove_empty_by_columns(dataframe, columns):
    print("\n")
    print(f"----- DELETING EMPTY ENTRIES FOR {columns}-----")

    string_dataframe = dataframe.applymap(str)
    no_space_df = string_dataframe.applymap(str.strip)
    no_empty_boolean_df = no_space_df[columns].ne("")
    no_empty_entries = no_empty_boolean_df.all(axis='columns')
    new_dataframe = dataframe[no_empty_entries]

    return new_dataframe


def main():
    parser = argparse.ArgumentParser()
    # Mandatory arguments
    parser.add_argument("data", help='Data file')
    # Optional arguments
    parser.add_argument(
        "-c",
        "--columns",
        nargs='+',
        help='Column(s) to remove [-c Column1 Column2]'
    )
    parser.add_argument("--output", help='CSV file output')
    parser.add_argument("--sep", help="Separator used in data if not comma [--sep '|']", default=',')
    args = parser.parse_args()

    data_file = args.data
    data_dataframe = pd.read_csv(data_file, sep=args.sep)

    # Check optionnal arguments
    if not args.columns:
        new_dataframe = remove_empty(data_dataframe)
    else:
        new_dataframe = remove_empty_by_columns(data_dataframe, args.columns)

    print(new_dataframe)
    new_number_rows = new_dataframe.shape[0]
    number_deleted_rows = int(data_dataframe.shape[0]) - int(new_number_rows)
    print(f"{number_deleted_rows} rows with empty entries have been deleted.")
    print("\n")

    if args.output:
        filename = args.output
    else:
        filename = f"{data_file.split('.')[0]}_removed_empty.csv"

    new_dataframe.to_csv(filename, index=False)


# Define what to do if file is run as script
if __name__ == "__main__":
    main()

import argparse

import pandas as pd
import matplotlib.pyplot as plt


def get_dataframe_info(dataframe):
    print("\n----- DATAFRAME INFORMATION -----")

    print(f"Columns: {dataframe.columns.values.tolist()}")
    print("")
    print(f"Shape: {dataframe.shape}")
    print("\n")


def get_null_dataframe(dataframe):
    null_bolean_df = dataframe.isnull()
    null_entries = null_bolean_df.any(axis='columns')
    null_dataframe = dataframe[null_entries]
    null_counts = null_bolean_df.sum()

    print(f"Number of null entries: {null_dataframe.shape[0]}")
    print("Null distribution:")
    print(null_counts)
    print("")
    print("Dataframe with null")
    print(null_dataframe)
    print("\n")

    return null_dataframe


def get_no_null_dataframe(dataframe):
    no_null_dataframe = dataframe.dropna(axis=0, how="any")
    number_columns = no_null_dataframe.shape[0]
    number_null = int(dataframe.shape[0]) - int(number_columns)

    print("----- NULL ENTRIES -----")
    print(f"{number_null} rows with null entries have been deleted.")
    print("\n")

    return no_null_dataframe


def get_empty_value_dataframe(dataframe):
    string_dataframe = dataframe.applymap(str)
    no_space_df = string_dataframe.applymap(str.strip)
    empty_boolean_df = no_space_df.eq("")
    empty_entries = empty_boolean_df.any(axis='columns')
    empty_values_df = dataframe[empty_entries]
    empty_counts = empty_boolean_df.sum()

    print(f"Number of empty rows: {empty_values_df.shape[0]}")
    print("Empty entries distribution:")
    print(empty_counts)
    print("")
    print("Dataframe with empty entries")
    print(empty_values_df)
    print("\n")
    empty_counts.plot(kind='barh')
    plt.title("Empty frequencies in CUSTOMERDB")
    plt.xlabel("FIELD")
    plt.ylabel("Number of empties")
    # plt.xticks(rotation=45)
    plt.show()

    return empty_values_df


def get_no_empty_value_dataframe(dataframe):
    string_dataframe = dataframe.applymap(str)
    no_space_df = string_dataframe.applymap(str.strip)
    no_empty_boolean_df = no_space_df.ne("")
    no_empty_entries = no_empty_boolean_df.all(axis='columns')
    no_empty_values_df = dataframe[no_empty_entries]
    number_columns = no_empty_values_df.shape[0]
    number_empty = int(dataframe.shape[0]) - int(number_columns)

    print("----- EMPTY ENTRIES -----")
    print(f"{number_empty} rows with empty entries have been deleted.")
    print("\n")

    return no_empty_values_df


def get_duplicates_dataframe(data_dataframe):
    duplicates_dataframe = data_dataframe[
        data_dataframe.duplicated()
    ]
    print(f"Number of duplicated entries: {duplicates_dataframe.shape[0]}")
    print("\n")

    return duplicates_dataframe


def get_no_duplicates_dataframe(dataframe):
    no_duplicates_df = dataframe.drop_duplicates()
    number_columns = no_duplicates_df.shape[0]
    number_duplicates = int(dataframe.shape[0]) - int(number_columns)

    print("----- DUPLICATED ENTRIES -----")
    print(f"{number_duplicates} duplicated rows have been deleted.")
    print("\n")

    return no_duplicates_df


def main():
    parser = argparse.ArgumentParser()

    # Mandatory arguments
    parser.add_argument("data", help='Data file')

    # Optional arguments
    parser.add_argument("--all", help='Remove every anomalies', action='store_true')
    parser.add_argument("--duplicates", help='Remove duplicates', action='store_true')
    parser.add_argument("--empty", help='Remove empty entries', action='store_true')
    parser.add_argument("--null", help='Remove null entries', action='store_true')
    parser.add_argument("--output", help='CSV file output [--output file.csv]')
    parser.add_argument("--sep", help="Separator used in data if not comma [--sep '|']", default=',')

    args = parser.parse_args()

    data_file = args.data
    data_dataframe = pd.read_csv(data_file, sep=args.sep)

    get_dataframe_info(data_dataframe)

    # Check optionnal arguments
    if args.duplicates or args.all:
        no_duplicates_df = get_no_duplicates_dataframe(data_dataframe)
        data_dataframe = no_duplicates_df
    else:
        get_duplicates_dataframe(data_dataframe)

    if args.null or args.all:
        no_null_df = get_no_null_dataframe(data_dataframe)
        data_dataframe = no_null_df
    else:
        get_null_dataframe(data_dataframe)

    if args.empty or args.all:
        no_empty_df = get_no_empty_value_dataframe(data_dataframe)
        data_dataframe = no_empty_df
    else:
        get_empty_value_dataframe(data_dataframe)

    if args.output:
        filename = args.output
    else:
        filename = f"{data_file.split('.')[0]}_prepared.csv"

    # Convert prepared dataframe to CSV file
    data_dataframe.to_csv(filename, index=False)


# Define what to do if file is run as script
if __name__ == "__main__":
    main()

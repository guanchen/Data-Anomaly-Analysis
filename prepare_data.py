import argparse
from datetime import datetime

import pandas as pd


def get_dataframe_info(dataframe):
    print("----- DATAFRAME INFORMATION -----")

    print("Columns: ")
    print(dataframe.columns)

    print("Shape: ")
    print(dataframe.shape)


def get_null_dataframe(dataframe):
    null_bolean_df = dataframe.isnull()
    null_entries = null_bolean_df.any(axis='columns')
    null_dataframe = dataframe[null_entries]

    print("----- DATAFRAME WITH NULL ENTRIES -----")
    print(null_dataframe)

    return null_dataframe


def get_empty_value_dataframe(dataframe):
    string_dataframe = dataframe.applymap(str)
    no_space_df = string_dataframe.applymap(str.strip)
    empty_boolean_df = no_space_df.eq("")
    empty_entries = empty_boolean_df.any(axis='columns')
    empty_values_df = dataframe[empty_entries]

    print("----- DATAFRAME WITH EMPTY ENTRIES -----")
    print(empty_values_df)

    return empty_values_df


def get_wrong_type_dataframe(data_dataframe, rules_dataframe):
    data = []
    for index, row in data_dataframe.iterrows():
        wrong_type = False
        data_row = []
        for item, value in row.iteritems():
            data_row.append(value)
            type = rules_dataframe.loc[item]['TYPE'].lower()
            if type == 'string':
                try:
                    float(value)
                    wrong_type = True
                except ValueError:
                    pass

            elif type == 'integer':
                try:
                    int(value)
                except ValueError:
                    wrong_type = True

            elif type == 'decimal':
                try:
                    float(value)
                except ValueError:
                    wrong_type = True
                    pass

            elif type == 'date':
                try:
                    datetime.strptime(value, '%Y-%m-%d')
                except ValueError:
                    try:
                        datetime.strptime(value, '%d-%m-%Y')
                    except ValueError:
                        wrong_type = True
                        pass

            elif type == 'time':
                try:
                    int(value)
                except ValueError:
                    wrong_type = True
                    pass

        if wrong_type:
            data.append(data_row)

    columns = []
    for index, row in rules_dataframe.iterrows():
        columns.append(index)

    wrong_type_df = pd.DataFrame(data, columns=columns)

    print("----- DATAFRAME WITH WRONG TYPE ENTRIES -----")
    print(wrong_type_df)

    return wrong_type_df


def get_duplicates_dataframe(data_dataframe, primary_key):
    print("----- DATAFRAME WITH DUPLICATED ENTRIES -----")
    # False if we want original and copy
    duplicates_dataframe = data_dataframe[
        data_dataframe.duplicated()
        # data_dataframe.duplicated(primary_key, "first")
    ]
    print(duplicates_dataframe)
    return duplicates_dataframe


def remove_duplicates_dataframe(data_dataframe):
    print("----- DATAFRAME AFTER DROPING DUPLICATED ENTRIES -----")

    no_duplicates_dataframe = data_dataframe.drop_duplicates()
    number_columns = no_duplicates_dataframe.shape[0]
    print(f"After dropping duplicates except for the first occurrence, the dataframe remains {number_columns} rows.")

    return no_duplicates_dataframe


def check_typos(data_dataframe):
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help='Data file')
    parser.add_argument("rules", help='Database rules file')
    parser.add_argument(
        "--primary_key",
        action='append',
        help="Primary key, can be called multiple times"
    )
    parser.add_argument("--sep", help='Separator', default='|')
    args = parser.parse_args()

    if not args.primary_key:
        print("You need to specify at least one primary key")
        exit()

    data_file = args.data
    rules_file = args.rules

    data_dataframe = pd.read_csv(data_file, sep=args.sep)
    rules_dataframe = pd.read_csv(rules_file, sep=args.sep)
    rules_dataframe = rules_dataframe.set_index('FIELD')

    get_dataframe_info(data_dataframe)
    get_null_dataframe(data_dataframe)
    get_empty_value_dataframe(data_dataframe)
    # get_wrong_type_dataframe(data_dataframe, rules_dataframe)
    get_duplicates_dataframe(data_dataframe, args.primary_key)
    remove_duplicates_dataframe(data_dataframe)


# Define what to do if file is run as script
if __name__ == "__main__":
    main()

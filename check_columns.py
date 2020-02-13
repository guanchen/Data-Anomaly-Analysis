import argparse

import pandas as pd


def check_columns(dataframe, source_columns, impacted_columns):
    conditions = ""

    source_conditions = ""
    first = True
    for source_column in source_columns:
        if first:
            source_conditions += f"{source_column}.str.strip().str.len() == 0 | {source_column}.isnull()"
            first: False
        else:
            source_conditions += f" | {source_column}.str.strip().str.len() == 0 | {source_column}.isnull()"

    second_conditions = ""
    first = True
    for impacted_column in impacted_columns:
        if first:
            second_conditions += f"{impacted_column}.str.strip().str.len() > 0"
            first: False
        else:
            second_conditions += f" | ({impacted_column}.str.strip().str.len() > 0)"

    conditions = f"({source_conditions}) & ({second_conditions})"
    print(conditions)
    abnormal_dataframe = dataframe.query(conditions)
    print(abnormal_dataframe)
    pass


def main():
    parser = argparse.ArgumentParser()
    # Mandatory arguments
    parser.add_argument("data", help='Data file')
    # Optional arguments
    parser.add_argument(
        "-cs",
        "--source_columns",
        nargs='+',
        help='Column(s) who impact other column(s) [-cs Column1 Column2]'
    )
    parser.add_argument(
        "-ci",
        "--impacted_columns",
        nargs='+',
        help='Column(s) impacted by source column(s) [-ci Column1 Column2]'
    )
    parser.add_argument("--output", help='CSV file output')
    parser.add_argument("--sep", help='Separator', default=',')
    args = parser.parse_args()

    data_file = args.data
    data_dataframe = pd.read_csv(data_file, sep=args.sep)

    # Check optionnal arguments
    if not args.source_columns and not args.impacted_columns:
        print("")
        exit(1)
    else:
        check_columns(data_dataframe, args.source_columns, args.impacted_columns)


# Define what to do if file is run as script
if __name__ == "__main__":
    main()

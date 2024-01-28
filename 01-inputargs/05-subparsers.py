import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        type=str,
        required=True,
        help="Database host"
    )
    parser.add_argument(
        "--user",
        type=str,
        required=True,
        help="Database user's name"
    )
    parser.add_argument(
        "--password",
        type=str,
        required=True,
        help="Database user's password"
    )
    parser.add_argument(
        "--schema",
        type=str,
        required=True,
        help="Database schema (name)"
    )
    subparsers = parser.add_subparsers(dest="operation", help="Database operation to perform")
    drop_parser = subparsers.add_parser("drop", help="Drop the database")
    drop_parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Do not ask, just do it!"
    )
    select_parser = subparsers.add_parser("select", help="Select records from the database")
    select_parser.add_argument(
        "--table",
        type=str,
        help="Table name"
    )
    select_parser.add_argument(
        "--records",
        type=int,
        help="Number of records to be selected"
    )
    insert_parser = subparsers.add_parser("insert", help="Insert values into the table")
    insert_parser.add_argument(
        "--table",
        type=str,
        help="Table name"
    )
    insert_parser.add_argument(
        "--values",
        type=str,
        metavar="VAL",
        nargs="+",
        help="Values to be inserted into the database"
    )
    args = parser.parse_args()
    print(args)
    if args.operation == "drop":
        print("Dropping database")
    elif args.operation == "select":
        print("Selecting records from the database")


if __name__ == '__main__':
    main()

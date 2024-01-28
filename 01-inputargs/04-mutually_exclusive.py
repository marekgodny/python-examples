import argparse
import time


def drop_db(database_schema: str):
    while True:
        answer = input(f"Are you sure you want to drop the database {database_schema}? y/n")
        if answer.lower() == "y":
            print(f"Dropping db schema = {database_schema}..")
            time.sleep(3)  # Database drop placeholder
            print(f"{database_schema} removed!")
            break
        elif answer.lower() == "n":
            break
        else:
            print("Please answer with \"y/n\" only!")
            continue


def select_records(records_num: int = 10):
    print(f"Returning {records_num} last records from the database...")
    time.sleep(2)  # Database select placeholder
    for i in range(records_num):
        print(f"\t{i}\tvalue_{i}")


def main():
    parser = argparse.ArgumentParser("DB commands execution")
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
        help="Database schema (name)"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--drop",
        action="store_true",
        help="Drop the database"
    )
    group.add_argument(
        "--select",
        type=int,
        help="Select N last records from the database"
    )
    args = parser.parse_args()
    print(args)
    if args.drop:
        drop_db(database_schema=args.schema)
    else:
        select_records(records_num=args.select)


if __name__ == "__main__":
    main()

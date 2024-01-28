import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", metavar="NAME", help="Your name")
    args = parser.parse_args()
    print(f"Hello {args.name}!")


if __name__ == '__main__':
    main()

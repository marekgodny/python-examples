import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mark", type=int, choices=range(1, 6))
    parser.add_argument("--move", choices=["left", "right", "up", "bottom"])
    # metavar
    parser.add_argument('--two_values', type=int, metavar="VAL", nargs=2)
    parser.add_argument('--zero_or_more', nargs="*", type=str)
    parser.add_argument('--one_or_more', nargs="+", type=int)
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()

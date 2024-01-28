import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Arguments parsing learn by example.')
    parser.add_argument('--verbose', '-v', action='count', default=0, help="verbosity level")
    args = parser.parse_args()
    log_levels = {
        0: "Error",
        1: "Warning",
        2: "Info",
        3: "Debug"
    }
    try:
        log_level = log_levels[args.verbose]
    except KeyError:
        log_level = log_levels[3]
    print(f"Logging level set to: {log_level}")

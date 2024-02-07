#!/usr/bin/python3
"""this module for stats"""
import sys


def print_metrics(total_size, status_codes):
    """Prints the computed metrics."""
    print("Total file size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


def main():
    total_size = 0
    status_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(total_size, status_counts)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in valid_codes:
                    status_counts[parts[-2]] = status_counts.get(parts[-2], 0) + 1
            except IndexError:
                pass

        print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()

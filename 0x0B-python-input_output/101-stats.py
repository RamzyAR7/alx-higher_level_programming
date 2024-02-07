#!/usr/bin/python3
"""this module for stats"""


import sys


def print_metrics(total_size, status_codes):
    """Prints the computed metrics."""
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_codes.items()):
        print("{}: {}".format(status_code, count))

def parse_line(line):
    """Parses a line and returns the file size and status code."""
    parts = line.split()
    return int(parts[-1]), parts[-2]

def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    try:
        for i, line in enumerate(sys.stdin, start=1):
            file_size, status_code = parse_line(line)
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            if i % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()

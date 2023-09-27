#!/usr/bin/python3
"""
Task: 0. Log Parsing
File: 0x06-log_parsing/0-stats.py
"""
from sys import stdin
import sys


def print_stats(total_size, status_code_counts):
    """
    This prints statistics at the beginning and every 10 lines
    This will also be called on a Keyboard interruption
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_code_counts[status_code]))

def parse_line(line):
    try:
        parts = line.split()
        if len(parts) >= 9:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            return status_code, file_size
    except ValueError:
        pass
    return None, None

total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        status_code, file_size = parse_line(line)
        if status_code is not None and file_size is not None:
            total_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_code_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_code_counts)
    raise
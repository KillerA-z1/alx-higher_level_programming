#!/usr/bin/python3

import sys
from collections import defaultdict

sts = defaultdict(int)
size = 0


def print_metrics():
    print(f"File size: {size}")
    for status, count in sorted(sts.items()):
        if count > 0:
            print(f"{status}: {count}")


try:
    for line_number, line in enumerate(sys.stdin, start=1):
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[-2]
            try:
                size += int(parts[-1])
                sts[status_code] += 1
            except (ValueError, IndexError):
                pass

        if line_number % 10 == 0:
            print_metrics()

    print_metrics()

except KeyboardInterrupt:
    print_metrics()
    raise

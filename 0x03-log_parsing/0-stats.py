#!/usr/bin/python3
"""Script for computing metrics(log parsing) from a stdin."""
# Create dict for status codes and their count.
# Set both status codes count and files total size to 0.
# Check if stdin line format is as expected,
# If not skip that line
# Check for existence of status codes in stdin
# If True, increment status codes count and total size of files read.
import sys


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
    }
count = 0
total_size = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            code = line_list[-2]
            file_size = int(line_list[-1])
            if code in status_codes.keys():
                status_codes[code] += 1

            total_size += file_size

            count += 1

        if count == 10:
            count = 0
            print("File size: {}".format(total_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))

except Exception as err:
    pass

finally:
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))

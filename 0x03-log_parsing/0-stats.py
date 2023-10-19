#!/usr/bin/python3
"""
Module: 0-stats

This module reads stdin line by line and computes matrics.
"""
import re
import sys
pattern1 = r'\d+\.\d+\.\d+\.\d+\s-\s\[\d+-\d+-\d+\s\d+:\d+:\d+\.\d+\]\s'
pattern2 = r'\"GET\s\/projects\/260\sHTTP\/1\.1\"\s\d\d\d\s\d+'
pattern = pattern1 + pattern2
line_number = 0
file_size = 0

dict_t = {
        200: 0, 301: 0, 400: 0,
        401: 0, 403: 0, 404: 0,
        405: 0, 500: 0
        }

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        # Process each line of input
        line = line.strip()  # Remove leading/trailing whitespace
        line_number += 1
        match = re.match(pattern, line)
        if not match:
            continue
        else:
            list_t = line.split()
            stat_code = int(list_t[7])
            if stat_code in dict_t:
                dict_t[stat_code] += 1
            file_size += int(list_t[8])
        if line_number == 10:
            print(f"File size: {file_size}")
            for key, value in sorted(dict_t.items()):
                if value != 0:
                    print(f'{key}: {value}')
            line_number = 0
except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for key, value in sorted(dict_t.items()):
        if value != 0:
            print(f'{key}: {value}')

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
count_200 = count_301 = count_400 = count_401 = 0
count_403 = count_404 = count_405 = count_500 = 0

dict_t = {
        200: count_200, 301: count_301, 400: count_400,
        401: count_401, 403: count_403, 404: count_404,
        405: count_405, 500: count_500
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
            if stat_code == 200:
                dict_t[200] += 1
            elif stat_code == 301:
                dict_t[301] += 1
            elif stat_code == 400:
                dict_t[400] += 1
            elif stat_code == 401:
                dict_t[401] += 1
            elif stat_code == 403:
                dict_t[403] += 1
            elif stat_code == 404:
                dict_t[404] += 1
            elif stat_code == 405:
                dict_t[405] += 1
            elif stat_code == 500:
                dict_t[500] += 1
            file_size += int(list_t[8])
        if line_number == 10:
            print(f"File size: {file_size}")
            for key, value in dict_t.items():
                if value != 0:
                    print(f'{key}: {value}')
            line_number = 0
except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for key, value in dict_t.items():
        if value != 0:
            print(f'{key}: {value}')

#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Heather Shilling


#read and analyze the logs

import re

from collections import defaultdict
from urllib.parse import urlparse

log_file_path = C:\Users\heath\Documents\Zen\GR Summer 2024\102\PythonforCybersecurity\start\CH07\access.log

with open (log_file_path, 'r') as file:
    log_lines = file.readlines()

print(log_lines)

status_code_counts = defaultdict(int)

for line in log_lines:
    match = re.search(r'\" \d{3} ', line')
    if match:
        status_code = match.group().strip().split()[1]
        status_code_counts[status_code] +=1

print("Status Code Distribution: ")

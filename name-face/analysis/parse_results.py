"""
    This file is used to parse the results of the nameface survey
    The first argument should be the file reference
    The second argument should be the output file

    #Note use >python3
"""
import csv
import sys
from parse_functions import *

file_ref = sys.argv[1]
output_file_ref = sys.argv[2]

excluded_columns = [
    'submitdate',
    'lastpage',
    'startlanguage',
    'intro',
]

keys = [
    'id',
    'Geslacht',
    'Geslacht[other]',
    'opleiding',
    'leeftijd',
    'opleiding[other]',
    'v1',
    'v1_group',
    'v2',
    'v2_group',
    'v3',
    'v3_group',
    'v4',
    'v4_group',
    'v5',
    'v5_group',
    'v6',
    'v6_group',
    'v7',
    'v7_group',
    'v8',
    'v8_group',
    'v9',
    'v9_group',
    'v10',
    'v10_group',
    'v11',
    'v11_group',
    'v12',
    'v12_group',
    'v13',
    'v13_group',
    'v14',
    'v14_group',
    'v15',
    'v15_group',
    'Eindvraag',
]
with open(file_ref, 'r', encoding='utf8') as file:
    csv_reader = csv.DictReader(file)
    with open(output_file_ref, 'w') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, keys, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for row in csv_reader:
            new_entry = parse_entry(row)
            w.writerow(new_entry)

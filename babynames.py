import sys
import re
import argparse


# /usr/bin/env python3
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
__author__ = "Timothy Reynoso with help from Howard"

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    names = []
    # +++your code here+++
    with open(filename) as file:
        raw_data = file.read()
    year = re.search(r'Popularity\sin\s(\d\d\d\d)', raw_data)
    if year:
        names.append(year.group(1))
    names_dict = {}
    name_and_rank = re.findall(
        r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', raw_data)
    for i in range(len(name_and_rank)):
        if name_and_rank[i][2] not in names_dict.keys():
            names_dict.update({name_and_rank[i][2]: name_and_rank[i][0]})
            # print(name_and_rank[i][2], name_and_rank[i][0])
        if name_and_rank[i][1] not in names_dict.keys():
            names_dict.update({name_and_rank[i][1]: name_and_rank[i][0]})
    updated_data = sorted(names_dict.items())
    for items in updated_data:
        names.append(f"{items[0]} {items[1]}")
    return names


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

    # +++your code here+++
    for file in file_list:
        file_name = f"{file}.summary"
        raw_result = '\n'.join(extract_names(file))
        # = '\n'.join(mylist)
        if create_summary:
            with open(file_name, "w+") as file:
                file.write(raw_result)

        print(raw_result)


if __name__ == '__main__':
    main(sys.argv[1:])

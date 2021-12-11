#!/usr/bin/env python3
# coding=utf-8
# Author: Milan Matyus

import os
import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-if", "--input_file", required=True, help="Path of the input file")
args = vars(ap.parse_args())


def line_count_by_wc(file_path):
    return int(os.popen("wc -l {}".format(file_path)).read().split()[0])


INPUT_FILE = args['input_file']
N = line_count_by_wc(INPUT_FILE)

bracket_pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
score_of_closing_bracket = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

with open(INPUT_FILE) as file_in:
    scores = list()
    for _ in range(N):
        bracket_string = file_in.readline().rstrip()
        required_close = list()
        # DEBUG: print(bracket_string)
        for bracket_char in bracket_string:
            if bracket_char in bracket_pairs.keys():
                required_close.append(bracket_pairs[bracket_char])
            if bracket_char in bracket_pairs.values():
                if bracket_char == required_close[-1]:
                    del required_close[-1]
                else:
                    # DEBUG: print("Expected " + required_close[-1] + ", but found " + bracket_char + " instead.")
                    scores.append(score_of_closing_bracket[bracket_char])
                    break
    print("Result: {}".format(sum(scores)))

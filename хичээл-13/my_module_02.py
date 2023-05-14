#!/usr/bin/python3

# My module 02

tutorials = ['c', 'c++', 'java', 'python', 'html', 'css', 'js']

def find_tutorial_very_long_name(target):
    for tut in tutorials:
        if tut == target:
            return True
    return False

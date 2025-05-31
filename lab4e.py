#!/usr/bin/env python3

# Name: lab4e.py
# Author: Chung Yin Choi
# Author ID: cychoi
# Date Created: 2025/05/31

def is_digits(sobj):
    count = 0
    for char in sobj:
        if char not in '0123456789':
            return False
    return True
    # place code here - loop through each character in sobj 

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')












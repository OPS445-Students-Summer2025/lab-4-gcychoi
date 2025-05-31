#!/usr/bin/env python3

# Name: lab4d.py
# Author: Chung Yin Choi
# Author ID: cychoi
# Date Created: 2025/05/31

# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(str):
    return str[0:5]
    # Place code here - refer to function specifics in section below

def last_seven(str):
    return str[-7:]
    # Place code here - refer to function specifics in section below

def middle_number(num):
    temp_str = str(num)
    return temp_str[1:3]
    # Place code here - refer to function specifics in section below

def first_three_last_three(str1,str2):
    return str1[0:3] + str2[-3:]
    # Place code here - refer to function specifics in section below


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))









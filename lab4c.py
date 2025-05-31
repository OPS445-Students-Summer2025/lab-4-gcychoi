#!/usr/bin/env python3

# Name: lab4c.py
# Author: Chung Yin Choi
# Author ID: cychoi
# Date Created: 2025/05/31

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    index = 0
    new_dict = {}
    while index != len(keys):
        new_dict[keys[index]] = values[index]
        index = index + 1
    return new_dict
    # Place code here - refer to function specifics in section below

def shared_values(dict1, dict2):
    new_list1 = []
    new_list2 = []
    for value in dict1.values():
        new_list1.append(value)
    for value in dict2.values():
        new_list2.append(value)        
    new_set1 = set(new_list1)        
    new_set2 = set(new_list2)
    return new_set1 & new_set2
    # Place code here - refer to function specifics in section below


if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)











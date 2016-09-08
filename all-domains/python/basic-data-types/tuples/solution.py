#!/usr/bin/env python
#https://www.hackerrank.com/challenges/python-tuples

number_of_elements = raw_input()
elements = raw_input()
elements_list = elements.split(' ')
elements_tuple = tuple([int(element) for element in elements_list])
hash_result = hash(elements_tuple)

print(hash_result)

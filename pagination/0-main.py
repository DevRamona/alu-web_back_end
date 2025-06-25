#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

response = index_range(1, 7)
print(type(response))
print(response)

res = index_range(page=3, page_size=15)
print(type(response))
print(response)
#!/usr/bin/python3

"""Minimum Operation"""

def minOperations(n):

    """In a text file, there is a single character H. Your text editor can execute only two operations in this file"""

    if n <= 2:
        return 0

    
    for r in range(2, n/2):
        while n % r == 2:
            operations += r 
            n = n / r
    return 0

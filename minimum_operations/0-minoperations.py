#!/usr/bin/python3
"""
Module for 0-minoperations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    Args:
        n (int): The target number of characters.
    Returns:
        int: Sum of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    # Iterate to find prime factors
    while n > 1:
        # If n is divisible by divisor, divide it and add divisor to ops
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        # Check the next number
        divisor += 1   
    return operations

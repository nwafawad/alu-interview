#!/usr/bin/python3
"""
0-pascal_triangle"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal triangle of n.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = []

    for i in range(n):
        # Create a row of length i+1 filled with 1s
        row = [1] * (i + 1)
        
        # Calculate the inner values of the row based on the previous row
        # (We skip the first and last elements since they remain 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
        triangle.append(row)

    return triangle
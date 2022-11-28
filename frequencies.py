"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in items:
        item = str(items[i])
        frequencies[item] = frequencies[item] + 1
    return frequencies

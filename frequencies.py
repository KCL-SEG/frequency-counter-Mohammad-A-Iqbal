"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items)):
            frequencies[items[i]] = frequencies[items[i]] + 1
    return frequencies

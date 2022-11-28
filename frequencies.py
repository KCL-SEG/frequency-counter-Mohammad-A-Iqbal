"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items)):
        if items[i] in frequencies:
            frequencies[items[i]] = frequencies[items[i]] + 1
        else:
            frequencies.update({items[i]: 1})
    return frequencies

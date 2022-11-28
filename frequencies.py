"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items)):
        item = str(items[int(i)])
        if item in frequencies:
            frequencies[item] = frequencies.get(item) + 1
        else:
            frequencies.update({item: 1}) 
    return frequencies

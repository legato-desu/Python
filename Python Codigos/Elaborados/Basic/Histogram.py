# Histogram
"""
Create a program to make a histogram from a list of integers
Analysis:
[2, 1, 5, 3]
* *
*
* * * * *
* * *
"""
def create_histogram (list, character ='* '):
    for e in list:
        print(character * e)
list = [2, 1, 5, 3]
create_histogram(list)
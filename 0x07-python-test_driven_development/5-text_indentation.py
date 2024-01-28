#!/usr/bin/python3
"""this modul for text_indentation function"""


def text_indentation(text):
    """this function print text"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']

    line = ""
    for char in text:
        line += char
        if char in punctuation_chars:
            print(line.strip())
            print()
            line = ""

    if line:
        print(line.strip())


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

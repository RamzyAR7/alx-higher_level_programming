#!/usr/bin/python3
"""this modul for text_indentation function"""


def text_indentation(text):
    """this function print text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for t in ".?:":
        text = (t + "\n\n").join(
            [line.strip(" ") for line in text.split(t)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers. """

def div(arr, low, high):
    """div and conquer"""

    med = int((high + low)/2)
    if arr[med-1] <= arr[med] >= arr[med+1]:
        return arr[med]
    elif arr[med] > arr[med+1]:
        return div(arr, low, med-1)
    elif arr[med] < arr[med+1]:
        return div(arr, med+1, high)


def find_peak(list_of_integers):
    """Find peak of a list"""

    if not list_of_integers:
        return None
    return div(list_of_integers, 0, len(list_of_integers)-1)

#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """this class only allows the creation of a first_name attribute"""
    __slots__ = ['first_name']

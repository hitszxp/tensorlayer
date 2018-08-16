#! /usr/bin/python
# -*- coding: utf-8 -*-

__all__ = ['force_return_self']


def force_return_self(func):
    """decorator to overwrite return value with `self` object"""

    def func_wrapper(self, *args, **kwargs):
        """decorator wrapper function"""
        func(self, *args, **kwargs)

        return self

    return func_wrapper
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Custom errors for unorderedlist.py
"""

class KeyErr(Error):
    """ Key not present in list """
    pass

class ValErr(Error):
    """ Key not present in list """
    pass

class ScopeErr(Error):
    """ Current index beyond list scope """
    pass

class ListEmpty(Error):
    """ List is empty """
    pass

#!/usr/bin/env python3

"""
List all the documents in colletion
"""



def list_all(mongo_collection):
    """
    A simple function to list all the documentss
    in a mongodb collection
    Args:
        mongo_collection (pymongo)
    """
    if mongo_collection:
        return list(mongo_collection.find())
    return []

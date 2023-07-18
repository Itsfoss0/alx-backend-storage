#!/usr/bin/env python3

"""
Insert a new document to a mongodb collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    A simple function to insert a document into a mongodb
    collection
    Args:
        mongo_collection (pymongo): the collection to insert into
        kwargs (dict): A dictionary representing the document
    """
    return mongo_collection.insert(kwargs)

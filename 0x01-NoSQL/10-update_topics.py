#!/usr/bin/env python3

"""
Change all topics of a school document
"""


def update_topics(mongo_collection, name, topics):
    """
    A simple function that update the values of a document
    """
    filter_ = {
        "name": name
    }

    new_topics = {
        "$set": {
            "topics": topics
        }
    }
    return mongo_collection.update_many(filter_, new_topics)

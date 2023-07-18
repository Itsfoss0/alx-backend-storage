#!/usr/bin/env python3

"""
Search schools by a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    A simple function to find documents that fit
    the matching search criteria
    Args:
        mongo_collection(pymongo): The collection
        topic (str): The topic to query for
    """

    topic_to_query = {
        "topics": topic
    }
    return mongo_collection.find(topic_to_query)

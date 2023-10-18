#!/usr/bin/env python3
"""script to update specific school records, re: their topics
`mongo_collection` will be the pymongo collection object
`name` (string) will be the school name to update
`topics` (list of strings) will be the list of topics approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """updates a specific record, by name, with new topics"""
    mongo_collection.update_many({"name": name},
                                {"$set": {"topics": topics}})

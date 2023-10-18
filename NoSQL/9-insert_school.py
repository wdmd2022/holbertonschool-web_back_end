#!/usr/bin/env python3
"""script to insert new doc in mongodb based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """inserts a doc based on the kwargs"""
    ll_new_doc = mongo_collection.insert_one(**kwargs)
    return ll_new_doc.inserted_id

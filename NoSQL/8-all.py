#!/usr/bin/env python3
# this file contains a function to list all docs in a collection


def list_all(mongo_collection):
    result = []
    for doc in mongo_collection.find():
        result.append(doc)
    return result

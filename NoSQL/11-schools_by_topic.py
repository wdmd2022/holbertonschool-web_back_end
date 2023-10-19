#!/usr/bin/env python3
""" this file contains a function to return a list of schools from mongo"""


def schools_by_topic(mongo_collection, topic):
    """"returns a list of docs that match a given topic field"""
    return list(mongo_collection.find({"topics": topic}))

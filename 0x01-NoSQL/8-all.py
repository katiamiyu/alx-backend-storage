#!/usr/bin/env python3
'''Doc module.
'''


def list_all(mongo_collection):
    '''returns documents in a collection.
    '''
    return [doc for doc in mongo_collection.find()]

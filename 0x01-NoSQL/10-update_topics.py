#!/usr/bin/env python3
'''doc module.
'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a collection using the name.
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

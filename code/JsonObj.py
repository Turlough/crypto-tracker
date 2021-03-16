import json


class JsonObj(object):
    """
    Utility class that self-converts a json string to a python object
    """

    def __init__(self, j):
        self.__dict__ = json.loads(j)

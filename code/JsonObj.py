import json


class Generic:
    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj


class JsonObj(object):
    """
    Utility class that self-converts a json string to a python object
    """

    def __init__(self, j):
        obj = json.loads(j, object_hook=Generic.from_dict)
        self.__dict__ = obj.__dict__

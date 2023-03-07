import json
import string
from random import randint, random, choices


def rstring():
    letters = string.ascii_letters
    return ''.join(choices(letters, k=randint(3, 10)))


def datatype(level, keys):
    t = randint(0, 6 - (level == 0) * 2)  # for every 7 type in json, if level is 0, then types are 5
    if t == 0:
        return rstring()
    elif t == 1:
        return randint(-255, 256)
    elif t == 2:
        return random() * randint(-255, 256)
    elif t == 3:
        return randint(0, 1) == 1
    elif t == 4:
        return None
    elif t == 5:
        return create_json(level - 1, keys)
    elif t == 6:
        return [datatype(level, keys) for _ in range(randint(0, 5))]


def create_json(level, keys):
    n_of_keys = randint(1, len(keys))
    n_r_keys = choices(keys, k=n_of_keys)
    js = {}
    for i in n_r_keys:
        js[i] = datatype(level, keys)
    return js


def generate_json(level, numkeys):
    return json.dumps(create_json(level, [rstring() for _ in range(numkeys)]))


def get_keys(js):
    t_dict = json.loads(js)
    a = [i for i in t_dict]
    return json.dumps(json.JSONEncoder().encode(a))


def search_dict_for_value(t_dict, value):
    a = []
    for i in t_dict:
        if i.__class__ == dict:
            a.__add__(search_dict_for_value(i, value))
        if i == value:
            a.append(i)
    return a


def find_value(js, value):
    t_dict = json.loads(js)
    a = search_dict_for_value(t_dict, value)
    return json.dumps(json.JSONEncoder.encode(a))


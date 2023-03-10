import json
import string
from random import randint, random, choices

from consts import MIN_KEY_LEN, MAX_KEY_LEN, MIN_RAND_INT, MAX_RAND_INT
from google.protobuf.json_format import MessageToDict, MessageToJson


def randstring():
    letters = string.ascii_letters
    return ''.join(choices(letters, k=randint(MIN_KEY_LEN, MAX_KEY_LEN)))


def datatype(level, keys):
    t = randint(0, 6 - (level == 0) * 2)  # for every 7 types in json, if level is 0, then types are 5
    if t == 0:
        return randstring()
    elif t == 1:
        return randint(-MIN_RAND_INT, MAX_RAND_INT)
    elif t == 2:
        return random() * randint(-MIN_RAND_INT, MAX_RAND_INT)
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
    return json.dumps(create_json(level, [randstring() for _ in range(numkeys)]))


def get_keys(js):
    t_dict = MessageToDict(js)
    a = [i for i in t_dict]
    return a


def search_dict_for_value(t_dict, value, error=None):
    a = []
    for i in t_dict:
        if t_dict[i].__class__ == dict:
            a.extend(search_dict_for_value(t_dict[i], value))
        if t_dict[i] == value:
            a.append(i)
        else:
            try:  # if value is int
                if t_dict[i] == int(value):
                    a.append(i)
            except ValueError:
                continue
    return a


def find_value(js, value):
    t_dict = MessageToDict(js)
    a = search_dict_for_value(t_dict, value)
    return a

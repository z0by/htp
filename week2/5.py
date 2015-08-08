def func(_dict):
    _new_dict = {}
    for key, value in _dict.iteritems():
        if _new_dict.get(value):
            if isinstance(_new_dict.get(value), list):
                _new_dict[value].extend([key])
            else:
                _new_dict[value] = list(_new_dict[value])
                _new_dict[value].extend([key])
        else:
            _new_dict[value] = key
    return _new_dict
_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 1, 'e': 0, 'u': 0}
print func(_dict)

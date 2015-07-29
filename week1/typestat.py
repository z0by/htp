def typestat(_list):
    _dict = {}
    for elem in _list:
        if _dict.get(type(elem)):
            _dict[type(elem)] += 1
        else:
            _dict[type(elem)] = 1
    for key,value in _dict.iteritems():
        print key,'=>',value

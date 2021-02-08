def getLocation(k, w, s):
    return 1, 2


def getMessage(messages):
    if len(messages['Kenobi']) != len(messages['Skywalker']) or len(messages['Kenobi']) != len(messages['Sato']):
        k, w, s = normalizeVectorsLength(messages['Kenobi'], messages['Skywalker'], messages['Sato'])
        return retrieveMessage(k, w, s)
    return retrieveMessage(messages['Kenobi'], messages['Skywalker'], messages['Sato'])


def messageAtPosition(kb, sw, st):
    out = kb
    if kb == "":
        if sw != "":
            out = sw
        elif st != "":
            out = st
    return out


def normalizeVectorsLength(k, w, s):
    normal = max(len(k), len(w), len(s))
    if len(k) < normal:
        k = normalizeVector(k, normal)
    if len(w) < normal:
        w = normalizeVector(w, normal)
    if len(s) < normal:
        s = normalizeVector(s, normal)
    return k, w, s


def normalizeVector(v, length):
    v = v + [""] * (length - len(v))
    return v


def retrieveMessage(kenobi, skywalker, sato):
    message = []
    for i in range(len(kenobi)):
        message.insert(i, messageAtPosition(kenobi[i], skywalker[i], sato[i]))
    if '' in message:
        print(message)
        raise Exception("Can't retrieve message")
    return ' '.join(message)


def createresponse(x, y, message):
    return {
        'position': {
            'x': x,
            'y': y
        },
        'message': message
    }

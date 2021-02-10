def message_at_position(kb, sw, st):
    out = kb
    if kb == "":
        if sw != "":
            out = sw
        elif st != "":
            out = st
    return out


def normalize_vectors_length(k, w, s):
    normal = max(len(k), len(w), len(s))
    if len(k) < normal:
        k = normalize_vector(k, normal)
    if len(w) < normal:
        w = normalize_vector(w, normal)
    if len(s) < normal:
        s = normalize_vector(s, normal)
    return k, w, s


def normalize_vector(v, length):
    v = v + [""] * (length - len(v))
    return v


def retrieve_message(kenobi, skywalker, sato):
    message = []
    for i in range(len(kenobi)):
        message.insert(i, message_at_position(kenobi[i], skywalker[i], sato[i]))
    if '' in message:
        print(message)
        raise Exception("Can't retrieve message")
    return ' '.join(message)

import rebels.trilateration as trilat
import rebels.msg_decode as decode


def get_location(k, w, s):
    return trilat.calculate_location(k, w, s)


def get_message(k, w, s):
    if len(k) != len(w) or len(k) != len(s):
        k, w, s = decode.normalize_vectors_length(k, w, s)
        return decode.retrieve_message(k, w, s)
    return decode.retrieve_message(k, w, s)


def create_response(x, y, message):
    return {
        'position': {
            'x': x,
            'y': y
        },
        'message': message
    }

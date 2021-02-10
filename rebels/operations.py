import rebels.trilateration as trilat
import rebels.msg_decode as decode


def get_location(k, w, s):
    return trilat.calculate_location(k, w, s)


def get_message(messages):
    if len(messages['Kenobi']) != len(messages['Skywalker']) or len(messages['Kenobi']) != len(messages['Sato']):
        k, w, s = decode.normalize_vectors_length(messages['Kenobi'], messages['Skywalker'], messages['Sato'])
        return decode.retrieve_message(k, w, s)
    return decode.retrieve_message(messages['Kenobi'], messages['Skywalker'], messages['Sato'])


def create_response(x, y, message):
    return {
        'position': {
            'x': x,
            'y': y
        },
        'message': message
    }

from django.http import HttpResponse, HttpResponseNotFound, \
    HttpResponseServerError, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import rebels.operations as ops
import rebels.satellites as sat

k = sat.Kenobi(0, '')
w = sat.Skywalker(0, '')
s = sat.Sato(0, '')


@csrf_exempt
def get_position_and_message(request):
    try:
        content = json.loads(request.body)
        satellites = content['satellites']

        for satellite in satellites:
            if satellite['name'] == 'kenobi':
                k.distance = satellite['distance']
                k.message = satellite['message']
            if satellite['name'] == 'skywalker':
                w.distance = satellite['distance']
                w.message = satellite['message']
            if satellite['name'] == 'sato':
                s.distance = satellite['distance']
                s.message = satellite['message']

        x, y = ops.get_location(k, w, s)
        message = ops.get_message(k.message, w.message, s.message)
        response = ops.create_response(x, y, message)
        return HttpResponse(json.dumps(response))
    except:
        return HttpResponseNotFound('Unable to find location or message')


@csrf_exempt
def get_position_and_message_split(request, satellite):
    if request.method == 'POST':
        content = json.loads(request.body)
        if satellite == 'Kenobi':
            k.distance = content['distance']
            k.message = content['message']
            return HttpResponse(k)
        if satellite == 'Skywalker':
            w.distance = content['distance']
            w.message = content['message']
            return HttpResponse(w)
        if satellite == 'Sato':
            s.distance = content['distance']
            s.message = content['message']
            return HttpResponse(s)
        else:
            return HttpResponseBadRequest('Invalid Method')
    else:
        return HttpResponseBadRequest('Invalid Method')


def retrieve_position_and_message(request):
    if request.method == 'GET':
        try:
            x, y = ops.get_location(k, w, s)
            message = ops.get_message(k.message, w.message, s.message)
            response = ops.create_response(x, y, message)
            return HttpResponse(json.dumps(response))
        except:
            return HttpResponseServerError('Unable to find location or message')
    else:
        return HttpResponseBadRequest('Invalid Method')


def dump_satellite_data(request):
    return HttpResponse('%s %s %s' % (repr(k), repr(w), repr(s)))

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

        messages = {'Kenobi': k.message, 'Skywalker': w.message, 'Sato': s.message}
        x, y = ops.get_location(k, w, s)
        response = ops.create_response(x, y, ops.get_message(messages))
        return HttpResponse(json.dumps(response))
    except:
        return HttpResponseNotFound('Error 404')


@csrf_exempt
def get_position_and_message_split(request, satellite):
    if request.method == 'POST':
        try:
            if satellite == 'Kenobi':
                return JsonResponse({"Kenobi": satellite})
            if satellite == 'Skywalker':
                return JsonResponse({"Skywalker": satellite})
            if satellite == 'Sato':
                return JsonResponse({"Sato": satellite})
            else:
                raise Exception()
        except:
            return HttpResponseNotFound('Not enough information')
    else:
        return HttpResponseBadRequest('Invalid Method')


def retrieve_position_and_message(request):
    if request.method == 'GET':
        return HttpResponse('GET Method')
    else:
        return HttpResponseBadRequest('Invalid Method')


def err(request):
    return JsonResponse({'Kenobi': 'X=' + str(sat.Kenobi.x) + " Y=" + str(sat.Kenobi.y)})

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import rebels.operations as ops
import rebels.satellites as sat

k = sat.Kenobi(0, '')
w = sat.Skywalker(0, '')
s = sat.Sato(0, '')


@csrf_exempt
def getpositionandmessage(request):
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
        x, y = ops.getLocation(k, w, s)
        response = ops.createresponse(x, y, ops.getMessage(messages))
        return HttpResponse(json.dumps(response))
    except:
        return HttpResponseNotFound('Error 404')


def index(request):
    print(w)
    try:
        return HttpResponse(str(w))
    except:
        return HttpResponseServerError()


def err(request):
    return JsonResponse({'Kenobi': 'X=' + str(sat.Kenobi.x) + " Y=" + str(sat.Kenobi.y)})

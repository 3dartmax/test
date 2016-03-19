from django.db.models.query import QuerySet
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse

def json_request(response):   # 파이어폭스 JSONView 플러그인설치.
    """
    #방법1.
    datas = []
    for data in response:
        datas.append({
            'id' : data.id,
            'title' : data.title,
            'content' : data.content,
            'created_date' : data.created_date
        })
    return JsonResponse(datas, safe=False, content_type='application/json')
    """
    """
    #방법2.
    datas = serialize('json', response)
    return HttpResponse(datas, content_type='application/json')
    """
    #방법3.
    datas = []
    for data in response:
        datas.append(data.getfields())
    return JsonResponse(datas, safe=False, content_type='application/json')


class JsonResponseMiddleware(object):
    def process_response(self, request, response):
        if isinstance(response, QuerySet):
            return json_request(response)
        return response

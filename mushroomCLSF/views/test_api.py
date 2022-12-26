from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


# Create your views here
@csrf_exempt
def test_function(request):
    if request.method == 'GET':
        data = json.loads(request.body)

        converted_data = {}
        for key, val in data.items():
            converted_data[key] = list(val)
        return JsonResponse(
            data=converted_data
        )


@csrf_exempt
def test(request):
    if request.method == 'GET':
        return JsonResponse(
            data={
                "name": "MUSHROOM"
            }
        )

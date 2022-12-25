from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


# Create your views here
@csrf_exempt
def test_function(request):
    if request.method == 'GET':
        return JsonResponse(
            data={
                "subject": "Kỹ nghệ tri thức",
                "backend": {
                    "framework": "django",
                    "deploy": ["vercel", "azure"]
                },
                "frontend": {
                    "framework": "react",
                    "deploy": ["vercel"]
                },
                "team member": [
                    {
                        "name": "Trần Đức Hiếu",
                        "realname": "Thiếu gia Quảng Ninh",
                        "characteristic": "Trùm web"
                    },
                    {
                        "name": "Trần Bảo Ngọc",
                        "realname": "Loli ...",
                        "characteristic": "Trùm AI Data"
                    },
                    {
                        "name": "Hoàng Mai Đức Long",
                        "realname": "Dài",
                        "characteristic": "Đại gia nhà đất Hoàng Mai",
                        "another": "Trùm đứng lên ngồi xuống"
                    },
                    {
                        "name": "VTD",
                        "realname": "The へたへたです",
                        "characteristic": "Làm phông bạt trang trí ...",
                    },
                ]
            }
        )


@csrf_exempt
def test(request):
    if request.method == 'GET':
        return JsonResponse(
            data={
                "name": "MUSHROOM"
            }
        )

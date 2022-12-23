from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
from mushroomCLSF.models import MushroomData


def classify():
    """ CLASSIFICATION CODE HERE """
    result = ""
    explanation = ""
    return result, explanation


@csrf_exempt
def naive_bayes_classify(request):
    if request.method == 'GET':
        data = json.loads(request.body)

        result, explanation = classify()
        return JsonResponse(
            data={
                "status": 200,
                "result": result,
                "explanation": explanation
            }
        )

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def classify():
    """ CLASSIFICATION CODE HERE """
    result = ""
    explanation = ""
    return result, explanation


@csrf_exempt
def decision_tree_classify(request):
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

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
import pandas as pd
from mushroomCLSF.datasets.mushrooms import load_mushrooms
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split
from mushroomCLSF.views.util import extract_data

def classify(data):
    """ CLASSIFICATION CODE HERE """
    data = {key: [value] for (key, value) in data.items()}
    input_features = list(data.keys())
    df, encode, decode = load_mushrooms(features=input_features, encode=True)
    input_df = pd.DataFrame.from_dict(data)
    for column in input_df:
        input_df[column] = encode(input_df, column)
    x_train, x_test, y_train, y_test = train_test_split(df[input_features], df['class'], random_state=42, test_size=0.2)
    model = CategoricalNB()
    model.fit(x_train, y_train)
    probas = model.predict_proba(input_df)[0]
    result = decode([max(range(len(probas)), key=probas.__getitem__)], column='class')[0]
    explanation = {decode([i], column="class")[0]: round(prob, 2)*100 for (i, prob) in enumerate(probas)}
    return result, explanation


@csrf_exempt
def naive_bayes_classify(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        converted = extract_data(data)
        result, explanation = classify(converted)
        return JsonResponse(
            data={
                "status": 200,
                "result": result,
                "explanation": explanation
            }
        )


if __name__ == '__main__':
    sample_request_data = {
        'cap-shape': 'x',
        'cap-surface': 's',
        'cap-color': 'n',
        'bruises': 't',
        'odor': 'p',
        'stalk-shape': 'e',
        'stalk-root': 'e',
        'spore-print-color': 'k',
        'habitat': 'u',
        'population': 's',
        'ring-type': 'p',
    }
    expected_label = 'p'
    res_label, explain = classify(sample_request_data)
    print(f'Expected result: {expected_label}')
    print(f'Result: {res_label}, Reason: {explain}')

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import pandas as pd
from mushroomCLSF.datasets.mushrooms import load_mushrooms
import numpy as np
from mushroomCLSF.views.util import extract_data


def get_decision_path(model, input_sample):
    node_indicator = model.decision_path(input_sample)
    leaf_id = model.apply(input_sample)
    feature = model.tree_.feature
    threshold = model.tree_.threshold
    feature_names = input_sample.columns.to_list()
    sample_id = 0
    # obtain ids of the nodes `sample_id` goes through, i.e., row `sample_id`
    node_index = node_indicator.indices[
                    node_indicator.indptr[sample_id]: node_indicator.indptr[sample_id + 1]
                 ]

    path = []
    for i, node_id in enumerate(node_index):
        # continue to the next node if it is a leaf node
        if leaf_id[sample_id] == node_id:
            continue

        # check if value of the split feature for sample 0 is below threshold
        if input_sample.values[sample_id, feature[node_id]] <= threshold[node_id]:
            threshold_sign = "<="
        else:
            threshold_sign = ">"

        response_threshold = str(threshold[node_id])
        response_no = int(i)
        response_node_id = int(node_id)
        response_feature = str(feature_names[feature[node_id]])
        response_value = str(input_sample.values[sample_id, feature[node_id]])
        response_inequality_sign = str(threshold_sign)

        path.append({
            'no': response_no,
            'node_id': response_node_id,
            'feature': response_feature,
            'value': response_value,
            'inequality_sign': response_inequality_sign,
            'threshold': response_threshold,
        })
    return path


def classify(data):
    """ CLASSIFICATION CODE HERE """
    data = {key: [value] for (key, value) in data.items()}
    input_features = list(data.keys())
    df, encode, decode = load_mushrooms(features=input_features, encode=True)
    input_df = pd.DataFrame.from_dict(data)
    for column in input_df:
        input_df[column] = encode(input_df, column)
    x_train, x_test, y_train, y_test = train_test_split(df[input_features], df['class'], random_state=42, test_size=0.2)
    model = DecisionTreeClassifier(criterion='entropy')
    model.fit(x_train, y_train)
    output = model.predict(input_df)
    result = decode(output, column='class')[0]
    explanation = get_decision_path(model, input_df)
    return result, explanation


@csrf_exempt
def decision_tree_classify(request):
    if request.method == 'POST':
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
        # 'bruises': 't',
        # 'odor': 'p',
        'stalk-shape': 'e',
        'stalk-root': 'e',
        'spore-print-color': 'k',
        'habitat': 'u',
        'population': 's',
        'ring-type': 'p',
    }
    expected_label = 'p'
    res_label, explain_text = classify(sample_request_data)
    print(f'Expected result: {expected_label}')
    print(f'Result: {res_label}\nReason: {explain_text}')

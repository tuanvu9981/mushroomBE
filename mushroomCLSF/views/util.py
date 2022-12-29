def extract_data(dictionary: dict) -> dict:
    new_obj = {}
    for key, value in dictionary.items():
        if value != "" and value != '':
            new_obj[key] = value
    return new_obj


# sample_request_data = {
#     'cap-shape': 'x',
#     'cap-surface': 's',
#     'cap-color': 'n',
#     'bruises': 't',
#     'odor': 'p',
#     'stalk-shape': 'e',
#     'stalk-root': 'e',
#     'spore-print-color': 'k',
#     'habitat': '',
#     'population': "",
#     'ring-type': 'p',
# }

# result = extract_data(sample_request_data)
# print(result)

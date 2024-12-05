def get_value_types(d):
    result = {}
    for key, value in d.items():
        if isinstance(value, dict):
            result[key] = get_value_types(value)
        else:
            result[key] = type(value)
    return result

# Словник 1
dict_1 = {
    "first_key": "first_value",
    "second_key": 123,
    "third_key": {
        "sub_key1": "sub_value1",
        "sub_key2": 45.67,
        "sub_key3": [1, 2, 3],
        "sub_key4": {"nested_key": "nested_value"},
        "sub_key5": True
    },
    "fourth_key": [10, 20, 30]
}
dict_types = get_value_types(dict_1)
print(dict_types)

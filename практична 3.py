# Словник 1
master_key = {
    "key_1": "text",
    "key_2": 123,
    "key_3": {
        "dubbed_key_1": "test_1",
        "dubbed_key_2": 12.34,
        "list_key_3": [1, 2, 3],
        "dubbed_key_4": {"str": "int"},
        "dubbed_key_5": True
    },
    "massive_key": [10, 20, 30]
}
types_key = {
"key_1": str,
    "key_2": int,
    "key_3": {
        "dubbed_key_1": str,
        "dubbed_key_2": float,
        "list_key_3": list,
        "dubbed_key_4": dict,
        "dubbed_key_5": bool,
    },
    "list_key": list
}

print(master_key)
print(types_key)


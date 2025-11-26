import json

data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
def is_correct_json(string):
    try:
        return bool(json.loads(string))
    except:
        return False
    
print(is_correct_json(data))
print(is_correct_json('number = 17'))
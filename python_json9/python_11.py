import json

with open("python_json8/food_services.json", "r", encoding="utf-8") as files:
    p_files = json.load(files)
    s = {}
    for row in p_files:
        s.setdefault(row["TypeObject"], []).append(row)       
    for k,v in s.items():
        s[k] = max(v,key=lambda x: x["SeatsCount"])  
    for k,v in sorted(s.items()):
        print(f'{k}: {v["Name"]}, {v["SeatsCount"]}')

    

    
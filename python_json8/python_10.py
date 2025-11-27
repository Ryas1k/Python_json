import json

with open("python_json8/food_services.json", "r", encoding="utf-8") as files:
    p_files = json.load(files)
    s = {}
    names = {}
    for row in p_files:
        s.setdefault(row["District"], []).append(row)
        if row["OperatingCompany"] != '':
          names[row["OperatingCompany"]] = names.get(row["OperatingCompany"], 0) + 1

    district_name, objects = max(s.items(), key=lambda x: len(x[1]))
    company_name, company_objects = max(names.items(),key=lambda x: x[1])
    print(f"{district_name}: {len(objects)}\n{company_name}: {company_objects}")
    
    
    
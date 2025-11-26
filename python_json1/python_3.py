import json

with open("python_json1\data1.json", "r", encoding="utf-8") as date1_file, open(
    "python_json1\data2.json", "r", encoding="utf-8"
) as date2_file:
    a = json.load(date1_file)
    b = json.load(date2_file)
    a.update(b)
    print(a)
with open("python_json1\data_merge.json", "w", encoding="utf-8") as data_merge_file:
    json.dump(a,data_merge_file, indent= 2)

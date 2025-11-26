import json

r = {}
with open("python_json3\countries.json", "r", encoding="utf-8") as files:
  countries = json.load(files)
  for c in countries:
    r.setdefault(c['religion'],[]).append(c["country"])

with open("python_json3/religion.json", "w", encoding="utf-8") as f:
  json.dump(r,f,indent=2)



    

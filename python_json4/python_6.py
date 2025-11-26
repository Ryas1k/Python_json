import json,csv

l = {}
with open('python_json4/playgrounds.csv','r',encoding='utf-8') as file_load:
  csv_file = csv.DictReader(file_load, delimiter=';')  
  for item in csv_file:
    l.setdefault(item['AdmArea'],{}).setdefault(item['District'],[]).append(item['Address'])

with open('python_json4/addresses.json','w',encoding='utf-8') as files:
  json.dump(l,files,indent=2,ensure_ascii=False)
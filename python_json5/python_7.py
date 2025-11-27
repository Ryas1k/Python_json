import csv,json

with open('python_json5\students.json','r',encoding='utf-8') as load_json:
  s = []
  json_load = json.load(load_json)  
  for item in json_load:
    if item['age'] >= 18 and item['progress'] >= 75:
      s.append({"name": item['name'], "phone": item['phone']})
  s.sort(key=lambda i: i['name'])

with open('python_json5/data.csv','w',encoding='utf-8',newline='') as f_csv:
  columns = ['name','phone'] 
  writer = csv.DictWriter(f_csv,delimiter=',',fieldnames=columns)
  writer.writeheader()
  for row in s:
    writer.writerow(row)
import json

with open('python_json2\people.json','r',encoding='utf-8') as people_file:
  peoples = json.load(people_file)
  res = {k: None for people in peoples for k in people}
  res1 = [res | people for people in peoples]
  
with open('python_json2/updated_people.json','w',encoding='utf-8') as updated_people_file:
  json.dump(res1,updated_people_file, indent=2)
  
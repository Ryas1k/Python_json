import sys, json

res = []
def decriptered(x):
  if type(x) == type(True):
    res.append(not x)
  elif type(x) == type(2) or type(x) == type(2.5):
    res.append(x + 1)
  elif type(x) == type([2,1]):
    res.append(x * 2)
  elif type(x) == type({'k':'v'}):
    x.update({"newkey": None})
    res.append(x)
  elif type(x) == type("str"):
    res.append(x + "!")  

with open('data.json','r',encoding='utf-8') as file:
  python_object = json.load(file)
  for item in python_object:
    decriptered(item)
  

with open('updated_data.json','w',encoding='utf-8') as file_w:
  json.dump(res,file_w)

 
       

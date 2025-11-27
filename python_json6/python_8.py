import json
from datetime import datetime,timedelta


def date_cal(i):
  forma = '%H:%M'
  s_const = datetime.strptime('10:00',forma)
  e_const = datetime.strptime('12:00',forma)
  start,end = i.split('-')
  start_pool = datetime.strptime(start,forma)
  end_pool = datetime.strptime(end,forma)
  if s_const == start_pool and  end_pool - e_const >=timedelta(0):
    pools.append(item)

with open('python_json6/pools.json','r',encoding='utf-8') as files:
  python_json = json.load(files)
  pools = []
  for item in python_json:
    date_cal(item['WorkingHoursSummer']['Понедельник'])
  m = max(pools,key= lambda x: (x["DimensionsSummer"]["Length"],x["DimensionsSummer"]["Width"]))
  
  print(f'{m["DimensionsSummer"]["Length"]}x{m["DimensionsSummer"]["Width"]}\n{m["Address"]}')
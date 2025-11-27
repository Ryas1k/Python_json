import json, csv

with open("python_json7\exam_results.csv", "r", encoding="utf-8", newline="") as files:
    reader = csv.DictReader(files, delimiter=",")
    grades = {}
    new_list = []
    for row in reader:
        grades.setdefault(row["email"], []).append(row)
    # проверка что студент может пересдать только 2 раза тоесть в сумме 3 сдачи может быть
    for k in grades:
        grades[k] = grades[k][:3]

    for key, value in grades.items():
        grades[key] = max(value, key=lambda x: (int(x["score"]), x["date_and_time"]))
        new_list.append(
            {
                "name": grades[key]["name"],
                "surname": grades[key]["surname"],
                "best_score": int(grades[key]["score"]),
                "date_and_time": grades[key]["date_and_time"],
                "email": grades[key]["email"]
            }
        )
    new_list.sort(key=lambda x: x["email"])
    
with open('python_json7/best_scores.json','w',encoding='utf-8') as create_files:
  json.dump(new_list,create_files,indent=2)

import json

data = {
    "football": [
        {"name": "Real Madrid", "country": "Spain", "total_win": 35},
        {"name": "Manchester United", "country": "England", "total_win": 20},
        {"name": "Bayern Munich", "country": "Germany", "total_win": 32},
        {"name": "Juventus", "country": "Italy", "total_win": 36},
        {"name": "Paris Saint-Germain", "country": "France", "total_win": 10}
    ]
}

with open("football.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

with open("football.json", "r", encoding="utf-8") as file:
    file_json = json.load(file)
    top_team = {
        'name': None,
        'country': None,
        'total_win': 0
    }
    print(file_json)
    for i in file_json['football']:
        if i['total_win'] > top_team['total_win']:
            top_team.update(i)
    print(f"Больше всего побед у команды {top_team['name']} из страны "
          f"{top_team['country']}. Кол-во побед: {top_team['total_win']}")

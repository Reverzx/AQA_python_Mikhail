import json
import re

data = {
    "football": [
        {"name": "Real Madrid", "country": "Spain", "titles_won": 35},
        {"name": "Manchester United", "country": "England", "titles_won": 20},
        {"name": "Bayern Munich", "country": "Germany", "titles_won": 32},
        {"name": "Juventus", "country": "Italy", "titles_won": 36},
        {"name": "Paris Saint-Germain", "country": "France", "titles_won": 10}
    ]
}

with open("football.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

with open("football.json", "r", encoding="utf-8") as file:
    file_str = file.read()
    name_pattern = r'"name":\s*"([^"]+)"'
    country_pattern = r'"country":\s*"([^"]+)"'
    won_pattern = r'"titles_won":\s*(\d+)'
    name_list = re.findall(name_pattern, file_str)
    country_list = re.findall(country_pattern, file_str)
    won_list = re.findall(won_pattern, file_str)
    index_of_max = won_list.index(max(won_list))
    print(f"Больше всего побед у команды {name_list[index_of_max]} из страны "
          f"{country_list[index_of_max]}. Кол-во побед: {won_list[index_of_max]}")

import requests
import random
import json
import time

BASE_URL = "https://api.opendota.com/api"

def get_data(endpoint):
    url = f"{BASE_URL}{endpoint}"
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()  
        return resp.json()
    except Exception as e:
        print(f"Ошибка: {e}")
        return None



def parse_prepare_data():
    all_data = []

    i = 1
    for i in range(155):
        print("hero_id: ", i, "\n")
        matches_list = get_data(f"/heroes/{i}/matches?limit=100") 

        if matches_list:
            print(f"Получено {len(matches_list)} матчей.")
            random_match = random.choice(matches_list)
            match_id = random_match['match_id']
    
            print(f"Случайный Match ID: {match_id}")
            obj = {"id_hero": i, "random_match": match_id, }
            all_data.append(obj)
        else:
            print("Не удалось получить список матчей.")
        time.sleep(1.2)

        with open("heroes_with_rndom_matches.json", "w", encoding="utf-8") as file:
            json.dump(all_data, file, ensure_ascii=False, indent=4)

parse_prepare_data()

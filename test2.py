import requests
import time

ACCOUNT_ID = 1288498532
BASE_URL = "https://api.opendota.com/api"

class User:
    def __init__(self):
        self.account_id = ACCOUNT_ID

    def get_matches(self):
        match_url = f"{BASE_URL}/players/{self.account_id}/matches"
        print("Запрашиваб данные о матчах")
        response = requests.get(match_url, timeout=15)
        response.raise_for_status()
        matches_list = response.json()
        for item in matches_list:
            print(item['match_id'])
            match_id = item['match_id']
            self.get_match_data(match_id)
            time.sleep(1.5)


    def get_match_data(self, match_id):
        match_data_url = f"{BASE_URL}/matches/{match_id}"
        print("просматриваю конкретный матч")
        response = requests.get(match_data_url, timeout=15)
        response.raise_for_status()
        match_data_list = response.json()
        print(match_data_url)
        print(match_data_list)
        


if __name__ == "__main__":
    user = User()
    user.get_matches()
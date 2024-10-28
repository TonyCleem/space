import requests
import os
import datetime
import argparse
from pathlib import Path
from dotenv import load_dotenv


def download_epic_photo(url, api_key):
    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    payload = {'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status
    json_data = response.json()
    for image_number, date_and_image in enumerate(json_data):
        date = date_and_image['date']
        image_name = date_and_image['image'] + '.png'
        adatetime = datetime.datetime.fromisoformat(date)
        formatted_date_1 = adatetime.strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date_1}/png/{image_name}"
        response = requests.get(url, params=payload)
        response.raise_for_status
        file_name = 'EPIC_photo_' + str(image_number) + '.png'
        file_path = path / file_name
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print('Загружено изображение EPIC_photo_'+str(image_number))


if __name__ == '__main__':
    load_dotenv()
    nasa_api = os.environ('NASA_API_TOKEN')
    url = 'https://epic.gsfc.nasa.gov/api/natural'
    download_epic_photo(url, nasa_api)

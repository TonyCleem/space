import requests
import pprint
import os
import datetime
import argparse
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import unquote, urlsplit


def get_image_from_nasa(url, api_key):
    directory = Path(r'C:\Devman\iso_tg\image')
    directory.mkdir(parents=True, exist_ok=True)

    payload = {'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status
    json_data = response.json()

    for image_number, date_and_image in enumerate(json_data):
        date = date_and_image['date']
        image_name = date_and_image['image'] + '.png'
        adatetime = datetime.datetime.fromisoformat(date)
        formatted_date_1 = adatetime.strftime("%Y/%m/%d")

        url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date_1}/png/{image_name}?api_key={api_key}"
        response = requests.get(url)
        response.raise_for_status

        file_name = 'EPIC_photo_' + str(image_number) + '.png'
        file_path = directory / file_name
    
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print('Загружено изображение EPIC_photo_'+str(image_number))


if __name__ == '__main__':
    load_dotenv()
    nasa_api = os.getenv('NASA_API')

    parser = argparse.ArgumentParser(description='Скачивает изображение с сайта NASA')
    parser.add_argument('-u', '--url', action='store_const', const='https://epic.gsfc.nasa.gov/api/natural', help='Подставляет предопределенный URL')
    args = parser.parse_args()

    get_image_from_nasa(args.url, nasa_api)

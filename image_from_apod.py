import requests
import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
from get_extension_on_link import get_an_extension


def image_from_apod(url, count, api_key):
    directory = Path(r'C:\Devman\space\image')
    directory.mkdir(parents=True, exist_ok=True)
    payload = {'count': count, 'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status
    json_data = response.json()
    
    for image_number, image_links in enumerate(json_data):
        link = image_links['url']
        extension= get_an_extension(link)
        response = requests.get(link)
        response.raise_for_status
        file_name = 'nasa_apod_' + str(image_number) + extension
        file_path = directory / file_name

        with open(file_path, 'wb') as file:
            file.write(response.content)
            print('Загружено изображение nasa_apod_'+str(image_number))


if __name__ == '__main__':
    load_dotenv()
    nasa_api = os.getenv('NASA_API')
    parser = argparse.ArgumentParser(description="Получить APOD с сайта NASA.")
    parser.add_argument(
        'count',
        nargs='?',         
        default='1',   
        help="Кол-во фото. Default = '1'"
    )
    directory = Path(r'C:\Devman\space\image')
    directory.mkdir(parents=True, exist_ok=True)
    args = parser.parse_args()
    url = 'https://api.nasa.gov/planetary/apod'
    image_from_apod(url, args.count, nasa_api)
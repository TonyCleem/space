import requests
import os
import argparse
from pathlib import Path
from dotenv import load_dotenv


def fetch_spacex_last_launch(url):
    directory = Path(r'C:\Devman\space\image')
    directory.mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status
    spacex_data = response.json()
    image_links = spacex_data['links']['flickr']['original']

    for image_number, link in enumerate(image_links):
        response = requests.get(link)
        response.raise_for_status
        file_name = 'spacex_' + str(image_number) + '.jpg'
        file_path = directory / file_name
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print('Загружено изображение spacex_'+str(image_number) + '.jpg')


if __name__ == '__main__':
    load_dotenv()
    nasa_api = os.getenv('NASA_API')

    url = 'https://api.spacexdata.com/v5/launches/'

    parser = argparse.ArgumentParser(description='Скачивает изображения с последнего запуска SpaceX')
    parser.add_argument('id', help='Подставляет указаный ID в URL')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.url, nasa_api)


    # key = 605b4b95aa5433645e37d041


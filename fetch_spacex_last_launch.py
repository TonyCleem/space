import requests
import os
import argparse
from pathlib import Path
from dotenv import load_dotenv


def fetch_spacex_last_launch(url, api):
    directory = Path(r'C:\Devman\space\image')
    directory.mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status
    spacex_data = response.json()
    image_links = spacex_data['links']['flickr']['original']
    if not image_links:
        print('Фотографий с последнего запуска нет')
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
    parser = argparse.ArgumentParser(description="Получить фото с запуска SpaceX")
    parser.add_argument(
        'id', 
        nargs='?',          
        default ='latest',
        help="ID запуска. Default = 'latest'"
    )
    args = parser.parse_args()

    url = f'https://api.spacexdata.com/v5/launches/{args.id}'
    print(url)
    fetch_spacex_last_launch(url, nasa_api)
import requests
import os
import datetime
import argparse
import pprint
from pathlib import Path
from dotenv import load_dotenv


def createParser ():
    parser = argparse.ArgumentParser(
        description="Скачивает фото Земли по указанной дате. По умолчнию скачает по последней дате."
        )
    parser.add_argument(
            'date',
            nargs='?',
            default=None,
            help="Дата в формате YYYY-MM-DD"
        )

    return parser


def formats_data(date):
    adatetime = datetime.datetime.fromisoformat(date)
    formatted_date_1 = adatetime.strftime("%Y/%m/%d")
    return formatted_date_1


def generates_url_nasa_epic(date, image_name):
    generated_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{image_name}"
    return generated_url


def downloades_images_from_epic(response):
    for image_number, date_and_image in enumerate(response):
        date = date_and_image['date']
        image = date_and_image['image']
        date = formats_data(date)
        image_name = f'{image}.png'
        generated_url = generates_url_nasa_epic(date, image_name)
        response = requests.get(generated_url)
        response.raise_for_status
        file_name = f'{image_name}'
        file_path = path / file_name
        with open(file_path, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    parser = createParser()
    args = parser.parse_args()
    date = args.date

    if not date:
        url = f'https://epic.gsfc.nasa.gov/api/natural'
        response = requests.get(url)
        response.raise_for_status
        response = response.json()
        downloades_images_from_epic(response)
        print('Загружены последние опубликованные фото')

    else:
        url = f'https://epic.gsfc.nasa.gov/api/natural/date/{date}'
        response = requests.get(url)
        response.raise_for_status
        response = response.json()
        downloades_images_from_epic(response)
        print(f'Загружены фото за {date}')
        


    





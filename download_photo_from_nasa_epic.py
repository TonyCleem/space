import datetime
import argparse
import requests
from pathlib import Path
from downloader import downloads_images_from_image_links
from fetch_images import get_images_from_api


def create_parser():
    parser = argparse.ArgumentParser(
        description="Скачивает фото Земли по указанной дате. По умолчнию скачает по последней дате."
        )
    parser.add_argument(
            'date',
            nargs='?',
            default='',
            help="Дата в формате YYYY-MM-DD"
        )

    return parser


def get_formatted_url(date, image_name):
    formatted_image_name = f'{image_name}.png'
    formatted_datetime = datetime.datetime.fromisoformat(date)
    formatted_date = formatted_datetime.strftime("%Y/%m/%d")
    formatted_url = f"https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/png/{formatted_image_name}"
    return formatted_url


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    date = args.date
    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    
    url = f'https://epic.gsfc.nasa.gov/api/natural/date/{date}'
    dates_and_image_names = get_images_from_api(url)
    image_links = [get_formatted_url(date_and_image_name['date'], date_and_image_name['image']) for date_and_image_name in dates_and_image_names]

    if downloads_images_from_image_links(image_links, path) and date:
        print(f'Загружены фото за {date}')
    else:
        print('Загружены последние опубликованные фото')
        
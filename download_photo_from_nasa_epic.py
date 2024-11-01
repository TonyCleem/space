import datetime
import argparse
from pathlib import Path
from fetch_data import get_json_data_from_api
from downloader import downloads_images_from_api


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


def creates_valid_image_links(epic_data):
    for date_and_file in epic_data:
        date = date_and_file['date']
        filename = date_and_file['image']
        image_name = f'{filename}.png'
        adatetime = datetime.datetime.fromisoformat(date)
        date = adatetime.strftime("%Y/%m/%d")
        generated_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{image_name}"
        image_links.append(generated_url)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    date = args.date
    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    
    image_links = []
    url = f'https://epic.gsfc.nasa.gov/api/natural/date/{date}'
    epic_data = get_json_data_from_api(url)
    creates_valid_image_links(epic_data)
    downloads_images_from_api(image_links, path)

    if not date:
        print('Загружены последние опубликованные фото')
    else:
        print(f'Загружены фото за {date}')
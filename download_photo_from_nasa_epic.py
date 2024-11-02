import datetime
import argparse
from pathlib import Path
from fetch_data import get_json_data_from_api
from downloader import downloads_images_from_images_links


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


def create_images_links_from_dates_and_images(epic_data):
    for date_and_image in epic_data:
        date = date_and_image['date']
        image = date_and_image['image']
        image_name = f'{image}.png'
        adatetime = datetime.datetime.fromisoformat(date)
        formatted_date = adatetime.strftime("%Y/%m/%d")
        formatted_url = f"https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/png/{image_name}"
        images_links.append(formatted_url)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    date = args.date
    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    
    images_links = []
    url = f'https://epic.gsfc.nasa.gov/api/natural/date/{date}'
    dates_and_images = get_json_data_from_api(url)
    create_images_links_from_dates_and_images(dates_and_images)
    downloads_images_from_images_links(images_links, path)

    if not date:
        print('Загружены последние опубликованные фото')
    else:
        print(f'Загружены фото за {date}')
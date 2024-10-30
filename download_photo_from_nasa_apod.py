import requests
import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
from filename_parser  import parse_filename_and_extension_from_url


def createParser ():
    parser = argparse.ArgumentParser(description="Получить Астрономческое фото дня с сайта NASA.")
    parser.add_argument(
        'count',
        nargs='?',         
        default='1',   
        help="Кол-во фото. Default = '1'"
    )

    return parser


def download_photo_from_url(url, count, token):
    payload = {'count': count, 'api_key': token}
    response = requests.get(url, params=payload)
    response.raise_for_status
    apod_info = response.json()
    for image_number, image_links in enumerate(apod_info):
        link = image_links['url']
        name, extension = parse_filename_and_extension_from_url(link)
        response = requests.get(link)
        response.raise_for_status
        file_name = f'APOD_is_{name}{extension}'
        file_path = path / file_name
        with open(file_path, 'wb') as file:
            file.write(response.content)

if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_API_TOKEN']
    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    parser = createParser()
    args = parser.parse_args()
    photo_count = args.count

    url = 'https://api.nasa.gov/planetary/apod'
    download_photo_from_url(url, photo_count, token)
    print(f'Загружено {photo_count} фото')
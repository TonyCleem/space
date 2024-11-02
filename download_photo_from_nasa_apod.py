import requests
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path
from fetch_and_decode_filename  import fetch_and_decodes_filename_from_link
from downloader import downloads_images_from_images_links


def create_parser():
    parser = argparse.ArgumentParser(description="Получить Астрономческое фото дня с сайта NASA.")
    parser.add_argument(
        'count',
        nargs='?',         
        default='1',   
        help="Кол-во фото. Default = '1'"
    )

    return parser


def get_images_url_from_api(url, image_count, api_key):
    payload = {'count': image_count, 'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images_url = response.json()
    return images_url
    

if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_TOKEN']
    parser = create_parser()
    args = parser.parse_args()
    image_count = args.count
    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    url = 'https://api.nasa.gov/planetary/apod'
    images_url = get_images_url_from_api(url, image_count, api_key)
    images_links = [link['url'] for link in images_url]
    downloads_images_from_images_links(images_links, path)
    print(f'Загружено {image_count} фото')
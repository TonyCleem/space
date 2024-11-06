import requests
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path
from downloader import downloads_images_from_image_links


def create_parser():
    parser = argparse.ArgumentParser(description="Получить Астрономческое фото дня с сайта NASA.")
    parser.add_argument(
        'count',
        nargs='?',         
        default='1',   
        help="Кол-во фото. Default = '1'"
    )

    return parser


def get_image_urls_from_api(url, image_count, api_key):
    payload = {'count': image_count, 'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    image_urls = response.json()
    return image_urls
    

if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_TOKEN']

    parser = create_parser()
    args = parser.parse_args()
    image_count = args.count

    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    
    url = 'https://api.nasa.gov/planetary/apod'
    image_urls = get_image_urls_from_api(url, image_count, api_key)
    image_links = [link['url'] for link in image_urls]
    downloads_images_from_image_links(image_links, path)
    print(f'Загружено {image_count} фото')
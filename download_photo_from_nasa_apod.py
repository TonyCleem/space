import requests
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path
from filename_parser  import parse_filename_and_extension_from_url
from downloader import downloads_images_from_api


def create_parser():
    parser = argparse.ArgumentParser(description="Получить Астрономческое фото дня с сайта NASA.")
    parser.add_argument(
        'count',
        nargs='?',         
        default='1',   
        help="Кол-во фото. Default = '1'"
    )

    return parser


def get_json_data_from_apod_api(url, count, api_token):
    payload = {'count': count, 'api_key': api_token}
    response = requests.get(url, params=payload)
    response.raise_for_status
    apod_json_data = response.json()
    return apod_json_data
    

if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_API_TOKEN']
    parser = create_parser()
    args = parser.parse_args()
    photo_count = args.count

    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    url = 'https://api.nasa.gov/planetary/apod'
    apod_json_data = get_json_data_from_apod_api(url, photo_count, nasa_token)
    image_links = [link['url'] for link in apod_json_data]
    downloads_images_from_api(image_links, path)
    print(f'Загружено {photo_count} фото')
    


   
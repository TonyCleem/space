import requests
import argparse
from pathlib import Path
from downloader import downloads_images_from_image_links
from fetch_images import get_images_from_api


def create_parser():
    parser = argparse.ArgumentParser(description="Получить фото с запуска SpaceX")
    parser.add_argument(
        'id', 
        nargs='?',          
        default ='latest',
        help="ID запуска. Default = 'latest'"
    )

    return parser


def get_image_links_from_last_launch(url):
    response = requests.get(url)
    response.raise_for_status
    launch_details = response.json()
    image_links = launch_details['links']['flickr']['original']
    return image_links


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    launch_id = args.id
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    if get_image_links_from_last_launch(url):
        path = Path('./image/')
        path.mkdir(parents=True, exist_ok=True)
        image_urls_from_launch = get_images_from_api(url)
        image_links = image_urls_from_launch['links']['flickr']['original']
        downloads_images_from_image_links(image_links, path)
        print('Загружены все фотографии с указанного ID запуска')
        
    if not get_image_links_from_last_launch(url):
        print('Фото с последнего запуска нет')

    
        
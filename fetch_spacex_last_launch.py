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


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    launch_id = args.id
    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
  

    images = get_images_from_api(url)
    image_links = images['links']['flickr']['original']

    if downloads_images_from_image_links(image_links, path):
        print('Загружены все фотографии с указанного ID запуска')
    else:    
        print('Фотографий с последнего запуска нет')
        




    
        

    

    
        
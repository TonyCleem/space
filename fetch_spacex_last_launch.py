import requests
import argparse
from pathlib import Path
from filename_parser  import parse_filename_and_extension_from_url


def createParser ():
    parser = argparse.ArgumentParser(description="Получить фото с запуска SpaceX")
    parser.add_argument(
        'id', 
        nargs='?',          
        default ='latest',
        help="ID запуска. Default = 'latest'"
    )

    return parser


def check_photo_from_last_launch(url):
    response = requests.get(url)
    response.raise_for_status
    launch_info = response.json()
    image_links = launch_info['links']['flickr']['original']
    return image_links


def download_images_from_launches(url, path):
    response = requests.get(url)
    response.raise_for_status
    launch_info = response.json()
    image_links = launch_info['links']['flickr']['original']
    for image_number, link in enumerate(image_links):
        name, extension = parse_filename_and_extension_from_url(link)
        response = requests.get(link)
        response.raise_for_status
        file_name = f'Photo_from_launch_{image_number}{extension}'
        file_path = path / file_name
        with open(file_path, 'wb') as file:
            file.write(response.content)
            

if __name__ == '__main__':
    path = Path('./image/')
    path.mkdir(parents=True, exist_ok=True)
    parser = createParser()
    args = parser.parse_args()
    launch_id = args.id
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    if not check_photo_from_last_launch(url):
        print('Фотографий с последнего запуска нет')
    else:
        download_images_from_launches(url, path)
        print('Загружены все фотографии с указанного запуска')
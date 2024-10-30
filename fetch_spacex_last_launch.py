import requests
import argparse
from downloader import download_files_from_data_in_dir
from directory_creator import creates_directory_for_image_path
from fetch_data import get_data_from_link


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
    data = response.json()
    images = data['links']['flickr']['original']
    return images


if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    launch_id = args.id
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    if not check_photo_from_last_launch(url):
        print('Фотографий с последнего запуска нет')
    else:
        path = creates_directory_for_image_path()
        data = get_data_from_link(url)
        links = data['links']['flickr']['original']
        download_files_from_data_in_dir(links, path)
        print('Загружены все фотографии с указанного ID запуска')
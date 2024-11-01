import requests
import argparse
from downloader import downloads_images_from_api_data
from fetch_data import get_json_data_from_api


def create_parser():
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
    api_spacex_data = response.json()
    images = api_spacex_data['links']['flickr']['original']
    return images


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    launch_id = args.id
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    if not check_photo_from_last_launch(url):
        print('Фотографий с последнего запуска нет')
    else:
        path = Path('./image/')
        path.mkdir(parents=True, exist_ok=True)
        api_spacex_data = get_data_from_link(url)
        links = api_spacex_data['links']['flickr']['original']
        download_files_from_data_in_dir(links, path)
        print('Загружены все фотографии с указанного ID запуска')
import requests
import os
import argparse
from dotenv import load_dotenv
from filename_parser  import parse_filename_and_extension_from_url
from downloader import download_files_from_data_in_dir
from directory_creator import creates_directory_for_image_path


def createParser ():
    parser = argparse.ArgumentParser(description="Получить Астрономческое фото дня с сайта NASA.")
    parser.add_argument(
        'count',
        nargs='?',         
        default='1',   
        help="Кол-во фото. Default = '1'"
    )

    return parser


def get_data_from_link(url, count, token):
    payload = {'count': count, 'api_key': token}
    response = requests.get(url, params=payload)
    response.raise_for_status
    data = response.json()
    return data
    

if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_API_TOKEN']
    parser = createParser()
    args = parser.parse_args()
    photo_count = args.count

    path = creates_directory_for_image_path()
    url = 'https://api.nasa.gov/planetary/apod'
    data = get_data_from_link(url, photo_count, token)
    image_links = []
    for link in data:
        image_link = link['url']
        image_links.append(image_link)
    download_files_from_data_in_dir(image_links, path)
    print(f'Загружено {photo_count} фото')
    


   
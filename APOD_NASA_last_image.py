import requests
import os
from pathlib import Path
from dotenv import load_dotenv


def get_image_from_apod(url, api_key):
    directory = Path(r'C:\Devman\space\image')
    directory.mkdir(parents=True, exist_ok=True)
    payload = {'count': '30', 'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status
    json_data = response.json()

    for image_number, image_links in enumerate(json_data):
        link = image_links['url']
        extension= get_an_extension(link)
        response = requests.get(link)
        response.raise_for_status
        file_name = 'nasa_apod_' + str(image_number) + extension
        file_path = directory / file_name

        with open(file_path, 'wb') as file:
            file.write(response.content)
            print('Загружено изображение nasa_apod_'+str(image_number))

if __name__ == '__main__':
    load_dotenv()
    nasa_api = os.getenv('NASA_API')

    url = 'https://api.nasa.gov/planetary/apod'
    get_image_from_apod(url, nasa_api)
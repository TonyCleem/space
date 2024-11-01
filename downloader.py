import requests
from filename_parser import parse_filename_and_extension_from_url


def downloads_images_from_api_data(api_data, path):
    for image_number, link in enumerate(api_data):
        name, extension = parse_filename_and_extension_from_url(link)
        response = requests.get(link)
        response.raise_for_status()
        file_name = f'Image_{name}{extension}'
        file_path = path / file_name
        with open(file_path, 'wb') as file:
            file.write(response.content)
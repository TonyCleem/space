import requests
from fetch_and_decode_filename import fetch_and_decodes_filename_from_link


def downloads_images_from_image_links(image_links, path):
    for image_number, link in enumerate(image_links):
        name, extension = fetch_and_decodes_filename_from_link(link)
        response = requests.get(link)
        response.raise_for_status()
        file_name = f'Image_{name}{extension}'
        file_path = path / file_name
        with open(file_path, 'wb') as file:
            file.write(response.content)



import requests
import os
from decoder_image_name_from_link import get_decoded_image_name_from_link


def downloads_images_from_image_links(image_links, path):
    if not image_links:
        return
    for link in image_links:
        response = requests.get(link)
        response.raise_for_status()
        decoded_image_name = get_decoded_image_name_from_link(link)
        name, extension = os.path.splitext(decoded_image_name)
        file_name = f'Image_{name}{extension}'
        file_path = path / file_name
        with open(file_path, 'wb') as file:
            file.write(response.content)
    return True



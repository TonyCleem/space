import os
from urllib.parse import unquote, urlsplit


def get_decoded_image_name_from_link(url):
    parsed_url = urlsplit(url)
    path = parsed_url.path
    filename = os.path.split(path)
    path, image_name = filename
    decoded_image_name = unquote(image_name)
    return decoded_image_name

import os
from urllib.parse import unquote, urlsplit


def fetch_and_decodes_filename_from_link(url):
    parsed_url = urlsplit(url)
    path = parsed_url.path
    filename = os.path.split(path)
    path, name = filename
    decoded_name = unquote(name)
    return os.path.splitext(decoded_name)
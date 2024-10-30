import os
from urllib.parse import unquote, urlsplit


def parse_filename_and_extension_from_url(url):
    parse = urlsplit(url)
    path = parse.path
    filename = os.path.split(path)
    path, name = filename
    decode = unquote(name)
    return os.path.splitext(name)
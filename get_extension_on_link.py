import os
from urllib.parse import unquote, urlsplit


def get_an_extension(url):
    parse = urlsplit(url)
    path = parse.path
    image_name = os.path.split(path)
    path, name = image_name
    decode = unquote(name)
    result = os.path.splitext(name)
    file, extension = result
    return extension
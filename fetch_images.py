import requests


def get_images_from_api(url):
    response = requests.get(url)
    response.raise_for_status
    images = response.json()
    return images
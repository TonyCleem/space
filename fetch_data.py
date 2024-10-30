import requests


def get_data_from_link(url):
    response = requests.get(url)
    response.raise_for_status
    return response.json()
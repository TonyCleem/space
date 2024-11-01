import requests


def get_json_data_from_api(url):
    response = requests.get(url)
    response.raise_for_status
    return response.json()
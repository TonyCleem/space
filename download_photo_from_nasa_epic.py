import datetime
import argparse
from fetch_data import get_data_from_link
from directory_creator import creates_directory_for_image_path
from downloader import download_files_from_data_in_dir


def createParser ():
    parser = argparse.ArgumentParser(
        description="Скачивает фото Земли по указанной дате. По умолчнию скачает по последней дате."
        )
    parser.add_argument(
            'date',
            nargs='?',
            default=None,
            help="Дата в формате YYYY-MM-DD"
        )

    return parser


def formats_data(date):
    adatetime = datetime.datetime.fromisoformat(date)
    formatted_date_1 = adatetime.strftime("%Y/%m/%d")
    return formatted_date_1


def generates_url_nasa_epic(date, image_name):
    generated_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{image_name}"
    return generated_url


def creates_image_links(data):
    for date_and_file in data:
        date = date_and_file['date']
        filename = date_and_file['image']
        image_name = f'{filename}.png'
        date = formats_data(date)
        image_links.append(generates_url_nasa_epic(date, image_name))


if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    date = args.date
    path = creates_directory_for_image_path()

    image_links = []
    if not date:
        url = f'https://epic.gsfc.nasa.gov/api/natural'
        data = get_data_from_link(url)
        creates_image_links(data)
        download_files_from_data_in_dir(image_links, path)
        print('Загружены последние опубликованные фото')
    else:
        url = f'https://epic.gsfc.nasa.gov/api/natural/date/{date}'
        data = get_data_from_link(url)
        creates_image_links(data)
        download_files_from_data_in_dir(image_links, path)
        print(f'Загружены фото за {date}')
import telegram
import random
import time
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser(
        description="Постит фото по указанному времени в часах."
        )
    parser.add_argument(
            'time',
            nargs='?',         
            default='4',
            type=int,  
            help="Время в часах. Default = '4ч'"
        )

    return parser


def get_images_of_directory(path):
    directory_structure = os.walk(path)
    for contents in directory_structure:
        dirpath, dirnames, images = contents
        return images


def sends_all_images_from_directory_by_timer(chat_id, path, images, hours):
    for image in images:
        time.sleep(hours)
        file_path = path / image
        with open(file_path, 'rb') as document:
            bot.send_document(chat_id, document)
        

def sends_image_by_timer(chat_id, path, image, hours):
        time.sleep(hours)
        file_path = path / image
        with open(file_path, 'rb') as document:
            bot.send_document(chat_id, document)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=tg_token)

    path = Path('./image/')

    parser = createParser()
    args = parser.parse_args()
    hours = args.time * 3600
    
    images = get_images_of_directory(path)
    if not images:
        print('Каталог пуст')
    else:
        sends_all_images_from_directory_by_timer(chat_id, path, images, hours)
        print('Все файлы из каталога отправлены. Начинается отправка случайных изображений из каталога')
    while True:
        images = get_images_of_directory(path)
        random.shuffle(images)
        image = images[0]
        sends_image_by_timer(chat_id, path, image, hours)
        print(f'Изображение {image} отправлено в телеграм канал {chat_id}')
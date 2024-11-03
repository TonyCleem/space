import telegram
import random
import time
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path
from directory_image_fetcher import get_images_of_directory


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


def sends_image_by_timer(bot, chat_id, path, image, hours):
        time.sleep(hours)
        file_path = path / image
        with open(file_path, 'rb') as document:
            bot.send_document(chat_id, document)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TELEGRAM_BOT_TOKEN']
    tg_channel_id = os.environ['TELEGRAM_CHANNEL_NAME']
    bot = telegram.Bot(token=tg_token)
    path = Path('./image/')
    parser = create_parser()
    args = parser.parse_args()
    hours = args.time * 3600
    
    images = get_images_of_directory(path)
    if not images:
        print('Каталог пуст')
    else:
        for image in images:
            sends_image_by_timer(bot, tg_channel_id, path, image, hours)
        print('Все файлы из каталога отправлены. Начинается отправка случайных изображений из каталога')
    while True:
        images = get_images_of_directory(path)
        random.shuffle(images)
        image = images[0]
        sends_image_by_timer(bot, tg_channel_id, path, image, hours)
        print(f'Изображение {image} отправлено в телеграм канал {tg_channel_id}')
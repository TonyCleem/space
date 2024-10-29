import telegram
import argparse
import os
import random
from dotenv import load_dotenv
from pathlib import Path


def createParser ():
    parser = argparse.ArgumentParser(
        description="Постит изображение в телеграм канал. При пустом ключе запостит случайное"
        )
    parser.add_argument(
            'file',
            nargs='?',
            default=None,
            help="<имя изображения>.<расширение>"
        )

    return parser


def get_images_of_directory(path):
    directory_structure = os.walk(path)
    for contents in directory_structure:
        dirpath, dirnames, images = contents
        return images


def sends_image(chat_id, path, image):
        with open(file_path, 'rb') as document:
            bot.send_document(chat_id, document)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=tg_token)
    updates = bot.get_updates()
    path = Path('./image/')

    parser = createParser()
    args = parser.parse_args()
    image = args.file

    if not image:
        images = get_images_of_directory(path)
        random.shuffle(images)
        image = images[0]
        file_path = path / image
        sends_image(chat_id, file_path, image)
        print(f'Изображение {image} отправлено на канал  {chat_id}')
    else:
        file_path = path / image
        sends_image(chat_id, file_path, image)
        print(f'Изображение {image} отправлено на канал  {chat_id}')
        
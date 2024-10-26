import telegram
import argparse
import os
import random
from dotenv import load_dotenv
from pathlib import Path

def posting_image():
    directory = Path(r'C:\Devman\space\image')
    changed_directory = os.walk(directory)
    for content in changed_directory:
        dirpath, dirnames, filenames = content
        random.shuffle(filenames)
        file = filenames[0]
        file_path = directory / file
        bot.send_document(chat_id='@window_on_space', document=open(file_path, 'rb'))
        print(f"Файл {file}' загружен")


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('TELEGRAM_API')
    bot = telegram.Bot(token=tg_token)
    updates = bot.get_updates()
    parser = argparse.ArgumentParser(
        description="Постит изображение в телеграм канал. При пустом ключе запостит случайное"
        )
    parser.add_argument(
            'file',
            nargs='?',
            default=None,
            help="<имя изображения>.<расширение>"
        )
    args = parser.parse_args()
    file = args.file
    if not file:
    	posting_image()
    else:
        directory = Path(r'C:\Devman\space\image')
        file = args.file
        file_path = directory / file
        bot.send_document(chat_id='@window_on_space', document=open(file_path, 'rb'))
        print(f"Файл {file}' загружен")
import telegram
import random
import time
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path


def posting_file():
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
    parser = argparse.ArgumentParser(
        description="Постит фото по указанному времени в часах."
        )
    parser.add_argument(
            'time',
            nargs='?',         
            default='4',   
            help="Время в часах. Default = '4ч'"
        )
    args = parser.parse_args()
    hours = int(args.time) * 3600
    while True:
        time.sleep(int(hours))
        posting_file()
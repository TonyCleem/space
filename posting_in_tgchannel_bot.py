import telegram
import random
import time
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path
from image_from_apod import image_from_apod


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
    bot = telegram.Bot(token='7827114156:AAFKhwQDyvOk8vLFnKuNp8WlHvByyzt3Wi8')
    parser = argparse.ArgumentParser(
        description="Постит фото по указанному времени в часах")
    parser.add_argument(
            'time',
            nargs='?',         
            default='4',   
            help="В параметрах укажите время, где 1 это 1 час"
        )
    args = parser.parse_args()
    hours = int(args.time) * 3600
    while True:
        time.sleep(hours)
        posting_file()
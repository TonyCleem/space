import telegram
import argparse
import os
import random
from dotenv import load_dotenv
from pathlib import Path

def posting_image():
    path = Path('./image/')
    changed_path = os.walk(path)
    for content in changed_path:
        dirpath, dirnames, filenames = content
        random.shuffle(filenames)
        file = filenames[0]
        file_path = path / file
        bot.send_document(chat_id, document=open(file_path, 'rb'))

if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
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
        path = Path('./image/')
        file = args.file
        file_path = path / file
        bot.send_document(chat_id, document=open(file_path, 'rb'))
        print(f"Файл {file}' загружен")
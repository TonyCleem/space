import telegram
import argparse
import os
import random
from directory_image_fetcher import get_images_of_directory
from sends_image import send_image_with_tg_bot
from dotenv import load_dotenv
from pathlib import Path


def create_parser():
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
    

if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TELEGRAM_BOT_TOKEN']
    tg_channel_id = os.environ['TELEGRAM_CHANNEL_NAME']

    bot = telegram.Bot(token=tg_token)
    updates = bot.get_updates()
    path = Path('./image/')
    parser = create_parser()
    args = parser.parse_args()
    image = args.file

    if not image:
        images = get_images_of_directory(path)
        random.shuffle(images)
        image = images[0]
        file_path = path / image
        send_image_with_tg_bot(bot, tg_channel_id, file_path)
        print(f'Изображение {image} отправлено на канал  {tg_channel_id}')
    else:
        file_path = path / image
        sends_image(bot, tg_channel_id, file_path)
        print(f'Изображение {image} отправлено на канал  {tg_channel_id}')
        
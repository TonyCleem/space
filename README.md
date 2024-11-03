# Space Scripts #
Приоткройте для себя окно в космос.
Вы можете открыть это окно для людей в своем канале Телеграм.


## Установка ##

#### Подготовка окружения

Python3 должен быть уже установлен.
Для корректной работы скрипта, рекомендую использовать все зависимости из файла `requirements.txt`
Запуск лучше производить используя виртуальное окружение `venv`.

Для создания `venv` и использования скрипта выполните следующее:


Создаем виртуальное окружение
```
python -m venv <name venv>
```

Активируем
```
<name venv>\Scripts\activate
```

Устанавливаем все зависимости из `requirements.txt`
```
pip install -r requirements.txt
```
В конце работы деактивируйте скрипт
```
deactivate
```

#### API

Для работы требуются токены API:
- [NASA](https://api.nasa.gov/#:~:text=Browse%20APIs-,Generate%20API%20Key,-Required%20fields%20are)

- [Telegram](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/#02:~:text=%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B8%C2%BB.-,%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%B5%D0%BC%20%D0%B1%D0%BE%D1%82%D0%B0,-%D0%A1%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B9%20%D1%88%D0%B0%D0%B3%20%E2%80%94%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5)

Полученные токены укажите в переменных файла `.env`.

Пример файла `.env`:
>```
>NASA_API=<ваш ключ>
>TELEGRAM_API=<токен от вашего бота>
>```

#### Telegram bot

Создаем бота через [BotFather](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)


## Использование ##

Для получения информации о работе каждого скрипта `-h`, `--help`.
```
py script -h
```


### Пример использования ###

#### `download_photo_from_nasa_epic`
Загружает сникми земли сделанные NASA. В качетсве ключа укажите дату (YYYY-MM-DD) или оставьте пустое значение, чтобы скачать последние снимки.
```cmd
C:\Devman\space>py download_photo_from_nasa_epic.py 1996-10-13
Загружены фото за 1996-10-13

C:\Devman\space>
```

#### `fetch_spacex_last_launch`
Скачивает фото с запуска SpaceX
Если у Вас есть ID запуска можете указать в качестве ключа. По умолчанию будут скачены фото с последнего запуска.
```cmd
C:\Devman\space>py fetch_spacex_last_launch.py 5eb87d47ffd86e000604b38a
Загружены все фотографии с указанного ID запуска

C:\Devman\space>
```

#### `download_photo_from_nasa_apod`
Скачивает "Astronomy Picture of the Day" (Астрономическую картину дня) или указанное кол-во изображений в ключе скрипта.
```cmd
C:\Devman\space>py download_photo_from_nasa_apod.py 3
Загружено 3 фото

C:\Devman\space>
```

#### Скрипты для телеграм бота
В файле `.env` укажите имя телеграм канала для переменной `tg_channel_id`.
>```
>NASA_API=<ваш ключ>
>TELEGRAM_API=<токен от вашего бота>
>tg_channel_id=<@имя_телеграм_канала>
>```


##### `send_images_bot`
Укажите имя изображения из директории как ключ. При пустом значении будет отправлено случайное
```cmd
C:\Devman\space>py send_images_bot.py Image_epic_1b_20241030091805.png
C:\Users\tonyc\AppData\Roaming\Python\Python312\site-packages\telegram\utils\request.py:46: UserWarning: python-telegram-bot is using upstream urllib3. This is allowed but not supported by python-telegram-bot maintainers.
  warnings.warn('python-telegram-bot is using upstream urllib3. This is allowed but not '
Изображение Image_epic_1b_20241030091805.png отправлено на канал  @window_on_space

C:\Devman\space>
```

##### `send_images_bot_with_timer`
Выгружает из директории все изображения в телеграм канал. Между постами оставляет промежуток времени.
Укажите время промежутка в качестве ключа, где 1 == 1 час. По умолчанию задано 4 часа между постами.
```cmd
C:\Devman\space>py send_images_bot_with_timer.py 2
C:\Users\tonyc\AppData\Roaming\Python\Python312\site-packages\telegram\utils\request.py:46: UserWarning: python-telegram-bot is using upstream urllib3. This is allowed but not supported by python-telegram-bot maintainers.
  warnings.warn('python-telegram-bot is using upstream urllib3. This is allowed but not '
Все файлы из каталога отправлены. Начинается отправка случайных изображений из каталога
Изображение Image_epic_1b_20241030144213.png отправлено в телеграм канал @window_on_space
Изображение Image_epic_1b_20241030144213.png отправлено в телеграм канал @window_on_space
Изображение Image_epic_1b_20241030144213.png отправлено в телеграм канал @window_on_space
```


## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
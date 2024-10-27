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
Во многих случах использования скриптов будет создана директория `C:\Devman\space\image` куда скачаются изображения.

#### `download_epic_photo`
Скачиает фото последние сники земли сделанные NASA

Ключи указывать не нужно. Достаточно запустить скрипт.
```cmd
(env) C:\Devman\space>py download_epic_photo.py
Загружено изображение EPIC_photo_0
Загружено изображение EPIC_photo_1
(env) C:\Devman\space>
```

#### `fetch_spacex_last_launch`
Скачивает фото с запуска SpaceX
Если у Вас есть ID запуска можете указать в качестве ключа. По умолчанию будут скачены фото с последнего запуска. Для подробностей используйте ключ `-h`
```cmd
(env) C:\Devman\space>py fetch_spacex_last_launch.py
https://api.spacexdata.com/v5/launches/latest
Фотографий с последнего запуска нет

(env) C:\Devman\space>
```

#### `image_from_apod`
Скачивает "Astronomy Picture of the Day" (Астрономическую картину дня) или указанное кол-во картин в ключе скрипта.
```cmd
(env) C:\Devman\space>py image_from_apod.py 3
Загружено изображение nasa_apod_0
Загружено изображение nasa_apod_1
Загружено изображение nasa_apod_2

(env) C:\Devman\space>
```

#### `image_posting_bot`

Требуется наличие телеграм бота токена. Скрипт выгружает случайную фотографию из директории `C:\Devman\space\image`.


В скрипте нужно указать имя группы для `chat_id`
```python
bot.send_document(chat_id='<@имя группы>', document=open(file_path, 'rb'))
```

Пример использования
```cmd
(env) C:\Devman\space>py image_posting_bot.py
C:\Devman\space\env\Lib\site-packages\telegram\utils\request.py:46: UserWarning: python-telegram-bot is using upstream urllib3. This is allowed but not supported by python-telegram-bot maintainers.
  warnings.warn('python-telegram-bot is using upstream urllib3. This is allowed but not '
Файл EPIC_photo_8.png' загружен

(env) C:\Devman\space>
```

#### `bot_timer_for_posting`

Задает таймер для размещения фотографий по указанному времени. Фотографии выбираются в случайном порядке из директории `C:\Devman\space\image`. По умолчанию задано 4 часа.


В скрипте нужно указать имя группы для `chat_id`
```python
bot.send_document(chat_id='<@имя группы>', document=open(file_path, 'rb'))
```

Пример использования
```cmd
(env) C:\Devman\space>py bot_timer_for_posting.py 3
C:\Devman\space\env\Lib\site-packages\telegram\utils\request.py:46: UserWarning: python-telegram-bot is using upstream urllib3. This is allowed but not supported by python-telegram-bot maintainers.
  warnings.warn('python-telegram-bot is using upstream urllib3. This is allowed but not '
Файл nasa_apod_1.jpg' выгружен на канал
Файл nasa_apod_2' выгружен на канал
Файл EPIC_photo_5.png' выгружен на канал
```


## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
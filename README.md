# Фото земли #

Скачивает последние снимки Земли сделанные NASA.


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

#### API NASA

Для работы скрипта требуется получить ключ API. Зарегистрируйтесь на сайте [API.NASA](https://api.nasa.gov/#:~:text=Browse%20APIs-,Generate%20API%20Key,-Required%20fields%20are) и получите ключ по указанной почте.


Полученный ключ укажите в переменной файла `.env` с именем `NASA_API`.

Пример файла `.env`:
>```
>NASA_API=<ваш ключ>
>```



## Использование ##

Для получения информации используйте `-h`, `--help`.
```
py vk.py -h
```



## Пример использования ##

>```
>(newvenv) C:\Devman\All leasons\OtherStudy\vk_app>py vk.py https://dvmn.org/modules
>https://vk.cc/cvPDMl
>
>(newvenv) C:\Devman\All leasons\OtherStudy\vk_app>
>```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
# Telegram бот “GeoQuiz”

## Продукт
Бот проводит викторины по географии на знание флагов и границ стран мира.
В своем проекте я использовал библиотеку `python-telegram-bot`, модуль `requests` для обращения
к `Yandex.Maps Static API`.
Границы стран я рисовал вручную по координатам и передавал эти данные в get-запрос для получения желаемого изображения
на карте.

## Описание

Бот предоставляет возможность любому пользователю мессенджера Telegram проверить свои знания в географии. Для
этого представляются две дисциплины: Флаги и Границы. В каждой дисциплине присутствует выбор трех уровней сложности.
После прохождения каждого теста пользователю будет предоставляться результат. Игрок имеет возможность сохранять и
обнулять свои данные по тестам. Для этого в моем проекте реализована связь с базой данных. Каждый пользователь в ней
записывается по уникальному id.

## Запуск

Для запуска моего проекта необходимо установить следующие библиотеки: `python-telegram-bot`, `requests`, которые
представлены в `requirements.txt`

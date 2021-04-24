from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
import os
import sqlite3
import sys
import requests
from token_data import TOKEN
from borders_encyclopedia import borders_encyclopedia

# global variables to keep user's data
LOGIN = False
user_result = 0
user_answers = list()


# the beginning of the quiz
def start(update, context):
    s1 = "Привет, я бот-географ. Я люблю проводить викторину, географические конечно."
    s2 = "Чтобы узнать мои возможности, введи /help"
    s3 = "Чтобы начать виторину, введи /start"
    s = '\n'.join([s1, s2, s3])
    update.message.reply_text(
        s, reply_markup=start_game_markup)
    return 1


# choosing quiz type
def game_choice(update, context):
    ans = update.message.text
    if ans.lower() not in ['flags', 'borders']:
        update.message.reply_text("Неправильные данные, начинай заново",
                                  reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    context.user_data['game'] = ans
    update.message.reply_text("Теперь выбери часть света:", reply_markup=continent_markup)
    return 2


# choosing the part of the world
def continent_choice(update, context):
    ans = update.message.text
    if ans.lower() not in ['europe', 'asia', 'africa', 'america']:
        update.message.reply_text("Неправильные данные, начинай заново",
                                  reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    context.user_data['continent'] = ans
    update.message.reply_text("Выбери уровень сложности:", reply_markup=difficulty_markup)
    return 3


# choosing the difficulty if the quiz
def diff_choice(update, context):
    ans = update.message.text
    if ans.lower() not in ['easy', 'medium', 'hard']:
        update.message.reply_text("Неправильные данные, начинай заново",
                                  reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    context.user_data['difficulty'] = ans
    f = context.user_data["game"].lower()
    update.message.reply_text("Нажмите Начать, чтобы приступить к викторине", reply_markup=beginning_markup)
    # starting the appropriate quiz
    if f.lower() == 'flags':
        return "Flags1"
    elif f.lower() == 'borders':
        return "Borders1"


def flag_quiz_1(update, context):
    try:
        src = list()
        # collecting data about the type of the quiz
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        # gathering images of flags
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[2]
        # sending flag to user
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))

        path += '/akeyboards.txt'
        # making the keyboard of answers
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[0].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return 'Flags2'
    # handling the unexpected error
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def flag_quiz_2(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        src = list()
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[3]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[1].strip().split(', ')
        ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
        ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return 'Flags3'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def flag_quiz_3(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        src = list()
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[4]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[2].strip().split(', ')
        ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
        ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return 'Flags4'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def flag_quiz_4(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        src = list()
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[5]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[3].strip().split(', ')
        ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
        ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return 'Flags5'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def flag_quiz_5(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        src = list()
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[6]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[4].strip().split(', ')
        ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
        ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return 'Flags6'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def flag_quiz_6(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        src = list()
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[7]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[5].strip().split(', ')
        ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
        ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return 'Flags7'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def flag_quiz_7(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        src = list()
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[8]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[6].strip().split(', ')
        ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
        ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return 'Flags8'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def flag_quiz_8(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        src = list()
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[9]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[7].strip().split(', ')
        ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
        ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return 'Flags9'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def flag_quiz_9(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        src = list()
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[10]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[8].strip().split(', ')
        ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
        ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return 'Flags10'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def flag_quiz_10(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        src = list()
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[11]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[9].strip().split(', ')
        ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
        ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return "Checkpoint"
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


# definition of the coordinates of the place
def get_ll(place):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b" \
                       f"&geocode={place}&format=json"
    response = requests.get(geocoder_request)
    # handling server's answer
    if response:
        json_response = response.json()

        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

        # Полный адрес топонима:
        lattitude = float(toponym["Point"]["pos"].split(' ')[1])
        longitude = float(toponym["Point"]["pos"].split(' ')[0])
        return f"{longitude},{lattitude}"
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")


def border_quiz_1(update, context):
    try:
        # collecting data about the type of the quiz
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/Flags/{s_dir}/{t_dir}'
        map_request = borders_encyclopedia[s_dir][t_dir][0]
        # getting appropriate image of the map
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        # sending flag to user
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(map_file, mode='rb'))

        path += '/akeyboards.txt'
        # making the keyboard of answers
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[0].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какая страна выделена на карте?", reply_markup=ans_mark)
        os.remove(map_file)
        return 'Borders2'
    # handling the unexpected error
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def border_quiz_2(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/Flags/{s_dir}/{t_dir}'
        map_request = borders_encyclopedia[s_dir][t_dir][1]
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(map_file, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[1].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какая страна выделена на карте?", reply_markup=ans_mark)
        os.remove(map_file)
        return 'Borders3'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def border_quiz_3(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/Flags/{s_dir}/{t_dir}'
        map_request = borders_encyclopedia[s_dir][t_dir][2]
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(map_file, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[2].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какая страна выделена на карте?", reply_markup=ans_mark)
        os.remove(map_file)
        return 'Borders4'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def border_quiz_4(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/Flags/{s_dir}/{t_dir}'
        map_request = borders_encyclopedia[s_dir][t_dir][3]
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(map_file, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            # выбираем нужную клавиатуру
            keys = file.readlines()[3].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какая страна выделена на карте?", reply_markup=ans_mark)
        os.remove(map_file)
        # вызываем следующий вопрос
        return 'Borders5'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def border_quiz_5(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/Flags/{s_dir}/{t_dir}'
        map_request = borders_encyclopedia[s_dir][t_dir][4]
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(map_file, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            # выбираем нужную клавиатуру
            keys = file.readlines()[4].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какая страна выделена на карте?", reply_markup=ans_mark)
        os.remove(map_file)
        # вызываем следующий вопрос
        return 'Borders6'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def border_quiz_6(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/Flags/{s_dir}/{t_dir}'
        map_request = borders_encyclopedia[s_dir][t_dir][5]
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(map_file, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            # выбираем нужную клавиатуру
            keys = file.readlines()[5].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какая страна выделена на карте?", reply_markup=ans_mark)
        os.remove(map_file)
        # вызываем следующий вопрос
        return 'Borders7'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def border_quiz_7(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/Flags/{s_dir}/{t_dir}'
        map_request = borders_encyclopedia[s_dir][t_dir][6]
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(map_file, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            # выбираем нужную клавиатуру
            keys = file.readlines()[6].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какая страна выделена на карте?", reply_markup=ans_mark)
        os.remove(map_file)
        # вызываем следующий вопрос
        return 'Borders8'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def border_quiz_8(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/Flags/{s_dir}/{t_dir}'
        map_request = borders_encyclopedia[s_dir][t_dir][7]
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(map_file, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            # выбираем нужную клавиатуру
            keys = file.readlines()[7].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какая страна выделена на карте?", reply_markup=ans_mark)
        os.remove(map_file)
        # вызываем следующий вопрос
        return 'Borders9'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def border_quiz_9(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/Flags/{s_dir}/{t_dir}'
        map_request = borders_encyclopedia[s_dir][t_dir][8]
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(map_file, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            # выбираем нужную клавиатуру
            keys = file.readlines()[8].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какая страна выделена на карте?", reply_markup=ans_mark)
        os.remove(map_file)
        # вызываем следующий вопрос
        return 'Borders10'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def border_quiz_10(update, context):
    try:
        global user_answers
        user_ans = update.message.text.lower()
        user_answers.append(user_ans)
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/Flags/{s_dir}/{t_dir}'
        path_to_data = path + '/ans.txt'
        map_request = borders_encyclopedia[s_dir][t_dir][9]
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(map_file, mode='rb'))

        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            # выбираем нужную клавиатуру
            keys = file.readlines()[9].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какая страна выделена на карте?", reply_markup=ans_mark)
        os.remove(map_file)
        # вызываем следующий вопрос
        return 'Checkpoint'
    except Exception as ex:
        update.message.reply_text("Извини, что-то пошло не так, но мы уже работаем над проблемой.",
                                  reply_markup=help_markup)
        print(ex)


def check_results(update, context):
    global user_answers, user_result, LOGIN
    user_ans = update.message.text.lower()
    user_answers.append(user_ans)
    f_dir = context.user_data["game"].capitalize()
    s_dir = context.user_data["continent"].capitalize()
    t_dir = context.user_data["difficulty"].capitalize()
    path = f'data/Flags/{s_dir}/{t_dir}/ans.txt'
    # opening file with right answers
    with open(path, mode='r', encoding='utf-8') as f:
        data = f.readlines()
        user_result = 0
        # checking user's answers
        for i in range(len(data)):
            if data[i].strip() == user_answers[i].strip():
                user_result += 1
        if user_result == 10:
            update.message.reply_text(
                f"Wow, да ты географический гений! 10 из 10! Продолжай в том же духе! Оцени викторину",
                reply_markup=rate_markup)
        else:
            update.message.reply_text(
                f"Твой результат: {user_result} из 10. Неплохо, но ты можешь лучше. Оцени викторину",
                reply_markup=rate_markup)
    user_answers.clear()
    # finishing the conversation
    if LOGIN:
        return "SaveResults"
    else:
        return 'restart'


# making a notes in database about the user
def login(update, context):
    global LOGIN
    # Подключение к БД
    con = sqlite3.connect("Achievement.sqlite")
    # Создание курсора
    cur = con.cursor()
    # identifying user's id
    x = str(update.message.chat_id)
    if not LOGIN:
        update.message.reply_text(
            "Супер, теперь твои результаты будут записываться, и ты сможешь узнать их, введя команду /info")
    else:
        # resetting case
        reques = f"""DELETE from progress WHERE id = {x}"""
        cur.execute(reques)
        con.commit()
        update.message.reply_text("Твои результаты полностью обнулены. Удачи!", reply_markup=help_markup)
    LOGIN = True
    # making notes about the user
    req = f"""INSERT INTO progress VALUES ({x}, 'Flags', 'Europe', 'Easy', 0), ({x}, 'Flags', 'Europe', 'Medium', 0), 
    ({x}, 'Flags', 'Europe', 'Hard', 0), ({x}, 'Flags', 'Asia', 'Easy', 0), ({x}, 'Flags', 'Asia', 'Medium', 0), 
    ({x}, 'Flags', 'Asia', 'Hard', 0), ({x}, 'Flags', 'Africa', 'Easy', 0), ({x}, 'Flags', 'Africa', 'Medium', 0), 
    ({x}, 'Flags', 'Africa', 'Hard', 0), ({x}, 'Flags', 'America', 'Easy', 0), 
    ({x}, 'Flags', 'America', 'Medium', 0), ({x}, 'Flags', 'America', 'Hard', 0),  
    ({x}, 'Borders', 'Europe', 'Easy', 0), ({x}, 'Borders', 'Europe', 'Medium', 0), 
    ({x}, 'Borders', 'Europe', 'Hard', 0), ({x}, 'Borders', 'Asia', 'Easy', 0), ({x}, 'Borders', 'Asia', 'Medium', 0), 
    ({x}, 'Borders', 'Asia', 'Hard', 0), ({x}, 'Borders', 'Africa', 'Easy', 0), ({x}, 'Borders', 'Africa', 'Medium', 0), 
    ({x}, 'Borders', 'Africa', 'Hard', 0), ({x}, 'Borders', 'America', 'Easy', 0), 
    ({x}, 'Borders', 'America', 'Medium', 0), ({x}, 'Borders', 'America', 'Hard', 0)"""
    # executing the request
    cur.execute(req)
    # commiting the changes
    con.commit()
    con.close()


def save_results(update, context):
    global user_result
    # Подключение к БД
    update.message.reply_text("Спасибо за оценку!", reply_markup=help_markup)
    con = sqlite3.connect("Achievement.sqlite")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    x = str(update.message.chat_id)
    # print(x)
    f_dir = context.user_data["game"].capitalize()
    s_dir = context.user_data["continent"].capitalize()
    t_dir = context.user_data["difficulty"].capitalize()
    val = cur.execute(f"""SELECT points from progress
    WHERE id = '{x}' AND type = '{f_dir}' AND location = '{s_dir}' AND difficulty = '{t_dir}'""").fetchone()
    request = f"""UPDATE progress
    SET points = {val[0] + user_result}
    WHERE id = '{x}' AND type = '{f_dir}' AND location = '{s_dir}' AND difficulty = '{t_dir}'"""
    cur.execute(request)
    con.commit()
    con.close()
    return ConversationHandler.END


# ending of the dialog
def restart(update, context):
    update.message.reply_text('Классно поиграли, хочешь еще раз?', reply_markup=help_markup)
    return ConversationHandler.END


# showing user's results
def info(update, context):
    global LOGIN
    if LOGIN:
        # connecting to the database
        con = sqlite3.connect("Achievement.sqlite")
        cur = con.cursor()
        # identifying user's id
        x = str(update.message.chat_id)
        request = f"""SELECT * from progress
        WHERE id = {x}"""
        # executing the request
        # gathering data
        res = cur.execute(request).fetchall()
        con.close()
        ans = list()
        # collecting user's data
        ans.append("Game | Location | Difficulty | Points")
        for r in res:
            s = f"{r[1]} | {r[2]} | {r[3]} | {r[4]}"
            ans.append(s)
        update.message.reply_text('\n'.join(ans), reply_markup=help_markup)
    else:
        # if user hasn't got any notes in the database
        update.message.reply_text(
            'Ты не зарегистрировался, поэтому я не слежу за твоими результатами. '
            'Чтобы исправить это введи команду /login')


# providing bot's skills to the user
def helper(update, context):
    s1 = 'Я - географический бот. Провожу викторины оп географии. Чтобы пройти викторину, нажми /start'
    s2 = 'Чтобы я запоминал твои результаты, введи /login'
    s3 = 'Чтобы увидель свои результаты, введи /info'
    s4 = 'Чтобы обнулить свои результаты, введи /reset'
    update.message.reply_text(
        "\n".join([s1, s2, s3, s4]),
        reply_markup=help_markup)


# quiting the dialog with the user
def stop(update, context):
    update.message.reply_text("Извините за беспокойство, до свидания", reply_markup=help_markup)
    return ConversationHandler.END


# handling unexpected messages
def unexpected_message(update, context):
    update.message.reply_text(f"Прости, я не понимаю, что ты имеешь в виду")


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    # parts of the world keyboard
    continent_keyboard = [['Europe', 'Asia'], ['America', 'Africa']]
    continent_markup = ReplyKeyboardMarkup(continent_keyboard, one_time_keyboard=False)

    # type of game keyboard
    start_game_keyboard = [['Flags', 'Borders']]
    start_game_markup = ReplyKeyboardMarkup(start_game_keyboard, one_time_keyboard=False)

    # keyboard for choosing difficulty
    difficulty_keyboard = [['Easy'], ['Medium', 'Hard']]
    difficulty_markup = ReplyKeyboardMarkup(difficulty_keyboard, one_time_keyboard=False)

    # the beginning of the quiz keyboard
    beginning_keyboard = [['Начать']]
    beginning_markup = ReplyKeyboardMarkup(beginning_keyboard, one_time_keyboard=False)

    # keyboard with nessacesary commands
    help_keyboard = [['/start', '/info', '/help']]
    help_markup = ReplyKeyboardMarkup(help_keyboard, one_time_keyboard=False)

    # keyboard for rating the quiz
    rate_keyboard = [['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐']]
    rate_markup = ReplyKeyboardMarkup(rate_keyboard, one_time_keyboard=False)

    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher
    print('Bot is waiting for you')
    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start', start)],
        # Точка прерывания диалога. В данном случае — команда /stop.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # beginning of the conversation
            1: [MessageHandler(Filters.text & ~Filters.command, game_choice, pass_user_data=True)],
            2: [MessageHandler(Filters.text & ~Filters.command, continent_choice, pass_user_data=True)],
            3: [MessageHandler(Filters.text & ~Filters.command, diff_choice, pass_user_data=True)],
            # borders cases
            "Borders1": [MessageHandler(Filters.text & ~Filters.command, border_quiz_1, pass_user_data=True)],
            "Borders2": [MessageHandler(Filters.text & ~Filters.command, border_quiz_2, pass_user_data=True)],
            "Borders3": [MessageHandler(Filters.text & ~Filters.command, border_quiz_3, pass_user_data=True)],
            "Borders4": [MessageHandler(Filters.text & ~Filters.command, border_quiz_4, pass_user_data=True)],
            "Borders5": [MessageHandler(Filters.text & ~Filters.command, border_quiz_5, pass_user_data=True)],
            "Borders6": [MessageHandler(Filters.text & ~Filters.command, border_quiz_6, pass_user_data=True)],
            "Borders7": [MessageHandler(Filters.text & ~Filters.command, border_quiz_7, pass_user_data=True)],
            "Borders8": [MessageHandler(Filters.text & ~Filters.command, border_quiz_8, pass_user_data=True)],
            "Borders9": [MessageHandler(Filters.text & ~Filters.command, border_quiz_9, pass_user_data=True)],
            "Borders10": [MessageHandler(Filters.text & ~Filters.command, border_quiz_10, pass_user_data=True)],
            # flags cases
            "Flags1": [MessageHandler(Filters.text & ~Filters.command, flag_quiz_1, pass_user_data=True)],
            "Flags2": [MessageHandler(Filters.text & ~Filters.command, flag_quiz_2, pass_user_data=True)],
            "Flags3": [MessageHandler(Filters.text & ~Filters.command, flag_quiz_3, pass_user_data=True)],
            "Flags4": [MessageHandler(Filters.text & ~Filters.command, flag_quiz_4, pass_user_data=True)],
            "Flags5": [MessageHandler(Filters.text & ~Filters.command, flag_quiz_5, pass_user_data=True)],
            "Flags6": [MessageHandler(Filters.text & ~Filters.command, flag_quiz_6, pass_user_data=True)],
            "Flags7": [MessageHandler(Filters.text & ~Filters.command, flag_quiz_7, pass_user_data=True)],
            "Flags8": [MessageHandler(Filters.text & ~Filters.command, flag_quiz_8, pass_user_data=True)],
            "Flags9": [MessageHandler(Filters.text & ~Filters.command, flag_quiz_9, pass_user_data=True)],
            "Flags10": [MessageHandler(Filters.text & ~Filters.command, flag_quiz_10, pass_user_data=True)],
            # end of conversation
            "restart": [MessageHandler(Filters.text & ~Filters.command, restart, pass_user_data=True)],
            "Checkpoint": [MessageHandler(Filters.text & ~Filters.command, check_results, pass_user_data=True)],
            "SaveResults": [MessageHandler(Filters.text & ~Filters.command, save_results, pass_user_data=True)]
        },
        fallbacks=[MessageHandler(Filters.regex('/stop'), stop)]
    )
    # activating dialog handler
    dp.add_handler(conv_handler)
    # adding user's commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', helper))
    dp.add_handler(CommandHandler('login', login))
    dp.add_handler(CommandHandler('reset', login))
    dp.add_handler(CommandHandler('info', info))
    # making message handler out of the dialog
    text_handler = MessageHandler(Filters.text, unexpected_message)
    # activating handler
    dp.add_handler(text_handler)
    # Регистрируем обработчик в диспетчере.
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()

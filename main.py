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

LOGIN = False
user_result = 0
user_answers = list()


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.


def start(update, context):
    s = "Привет, я бот-географ. Я люблю проводить викторину, географические конечно.\nДавай сыграем! Выбери викторину:"
    update.message.reply_text(
        s, reply_markup=start_game_markup)
    return 1


def game_choice(update, context):
    ans = update.message.text
    if ans.lower() not in ['flags', 'borders']:
        update.message.reply_text("Неправильные данные, начинай заново",
                                  reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    context.user_data['game'] = ans
    update.message.reply_text("Теперь выбери континент:", reply_markup=continent_markup)
    return 2


def continent_choice(update, context):
    ans = update.message.text
    if ans.lower() not in ['europe', 'asia', 'africa', 'south america', 'northern america']:
        update.message.reply_text("Неправильные данные, начинай заново",
                                  reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    context.user_data['continent'] = ans
    update.message.reply_text("Выбери уровень сложности:", reply_markup=difficulty_markup)
    return 3


def diff_choice(update, context):
    ans = update.message.text
    if ans.lower() not in ['easy', 'medium', 'hard']:
        update.message.reply_text("Неправильные данные, начинай заново",
                                  reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    context.user_data['difficulty'] = ans
    f = context.user_data["game"].lower()
    update.message.reply_text("Нажмите Начать, чтобы приступить к викторине", reply_markup=beginning_markup)
    if f.lower() == 'flags':
        return "Flags1"
    elif f.lower() == 'borders':
        return "Borders1"


def flag_quiz_1(update, context):
    try:
        src = list()
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        for currentdir, dirs, files in os.walk(path):
            src = files
        path_to_photo = path + '/' + src[2]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path_to_photo, mode='rb'))
        path += '/akeyboards.txt'
        with open(path, mode='r', encoding='utf-8') as file:
            keys = file.readlines()[0].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        return 'Flags2'
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


def get_ll(place):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b" \
                       f"&geocode={place}&format=json"
    response = requests.get(geocoder_request)
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
        f_dir = context.user_data["game"].capitalize()
        s_dir = context.user_data["continent"].capitalize()
        t_dir = context.user_data["difficulty"].capitalize()
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        path_to_data = path + '/ans.txt'
        with open(path_to_data, mode='r', encoding='utf8') as data:
            names = data.readlines()
        coords = get_ll(names[0].strip())
        map_request = f"https://static-maps.yandex.ru/1.x/?ll={coords}&l=sat&pl=c:ffff0000,bw:1,w:2," \
                      f"1.988267,51.012369,8.005279,48.957596,7.385603,47.563411,5.922205,46.228316," \
                      f"6.673080,46.412218,6.572156,45.183963,7.440102,43.782379,6.250702,43.132392," \
                      f"4.259497,43.467014,3.363289,43.286582,0.689137,42.861991,0.581576,42.727936," \
                      f"-1.779820,43.368730,-1.160999,46.167456,-4.744144,48.528866,-1.407616,48.663615," \
                      f"-1.532320,49.667046,-0.107681,49.295354,1.988267,51.012369"
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
            keys = file.readlines()[0].strip().split(', ')
            ans_key = [[keys[0], keys[1]], [keys[2], keys[3]]]
            ans_mark = ReplyKeyboardMarkup(ans_key, one_time_keyboard=False)
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        os.remove(map_file)
        return 'Borders2'
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
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        path_to_data = path + '/ans.txt'
        with open(path_to_data, mode='r', encoding='utf8') as data:
            names = data.readlines()
        coords = get_ll(names[1].strip())
        map_request = f"https://static-maps.yandex.ru/1.x/?ll={coords}&l=sat&pl=c:ffff0000,bw:1,w:2," \
                      f"7.569078,43.910962,6.747364,45.075701,7.015151,45.879271,7.960765,46.000090," \
                      f"8.450661,46.442929,8.997522,45.785294,10.159601,46.261484,10.626712,46.827464," \
                      f"13.611661,46.545216,12.130579,45.321053,13.575204,43.515401,18.381438,39.906873," \
                      f"17.032516,40.556523,16.451476,39.910382,17.121128,38.955071,15.007553,36.698615," \
                      f"12.514617,38.071556,15.538655,38.240585,15.793369,39.879831,10.661173,43.020464," \
                      f"10.113811,44.049483,8.921538,44.458467,8.189916,44.069024,7.569078,43.910962"
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
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
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
        path = f'data/{f_dir}/{s_dir}/{t_dir}'
        path_to_data = path + '/ans.txt'
        with open(path_to_data, mode='r', encoding='utf8') as data:
            names = data.readlines()
        coords = get_ll(names[2].strip())
        map_request = f"https://static-maps.yandex.ru/1.x/?ll={coords}&l=sat&pt=7.231986,61.400856,pm2rdm" \
                      f"&pl=c:ffff0000,bw:1,w:2," \
                      f"30.718656,69.747546,28.968125,69.149642,28.977413,69.731236,25.828935,69.646006," \
                      f"25.011148,68.678082,23.171129,68.707824,21.658224,69.301635,20.002206,69.060187," \
                      f"19.924517,68.381488,18.268499,68.593100,17.880050,68.002911,17.184932,68.132849," \
                      f"14.412636,66.176211,13.619382,64.590908,12.008342,63.607401,10.593592,59.111509"
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
        update.message.reply_text("Какой стране принадлежит этот флаг?", reply_markup=ans_mark)
        os.remove(map_file)
        return 'Borders4'
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
    path = f'data/{f_dir}/{s_dir}/{t_dir}/ans.txt'
    with open(path, mode='r', encoding='utf-8') as f:
        data = f.readlines()
        user_result = 0
        for i in range(len(data)):
            if data[i].strip() == user_answers[i].strip():
                user_result += 1
        if user_result == 10:
            update.message.reply_text(
                f"Wow, да ты географический гений! 10 из 10! Продолжай в том же духе! Оцени викторину",
                reply_markup=help_markup)
        else:
            update.message.reply_text(
                f"Твой результат: {user_result} из 10. Неплохо, но ты можешь лучше. Оцени викторину",
                reply_markup=rate_markup)
    user_answers.clear()
    if LOGIN:
        return "SaveResults"
    else:
        return ConversationHandler.END


def login(update, context):
    global LOGIN
    if not LOGIN:
        update.message.reply_text(
            "Супер, теперь твои результаты будут записываться, и ты сможешь узнать их, введя команду /info")
    else:
        update.message.reply_text("Твои результаты полностью обнулены. Удачи!")
    LOGIN = True

    # Подключение к БД
    con = sqlite3.connect("Achievement.sqlite")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    x = str(update.message.chat_id)
    req = f"""INSERT INTO progress VALUES ({x}, 'Flags', 'Europe', 'Easy', 0), ({x}, 'Flags', 'Europe', 'Medium', 0), ({x}, 'Flags', 'Europe', 'Hard', 0), 
({x}, 'Flags', 'Asia', 'Easy', 0), ({x}, 'Flags', 'Asia', 'Medium', 0), ({x}, 'Flags', 'Asia', 'Hard', 0), 
({x}, 'Flags', 'Africa', 'Easy', 0), ({x}, 'Flags', 'Africa', 'Medium', 0), ({x}, 'Flags', 'Africa', 'Hard', 0), 
({x}, 'Flags', 'South America', 'Easy', 0), ({x}, 'Flags', 'South America', 'Medium', 0), ({x}, 'Flags', 'South America', 'Hard', 0), 
({x}, 'Flags', 'Northern America', 'Easy', 0), ({x}, 'Flags', 'Northern America', 'Medium', 0), ({x}, 'Flags', 'Northern America', 'Hard', 0)"""
    cur.execute(req)
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
    print(val[0], user_result)
    request = f"""UPDATE progress
    SET points = {val[0] + user_result}
    WHERE id = '{x}' AND type = '{f_dir}' AND location = '{s_dir}' AND difficulty = '{t_dir}'"""
    cur.execute(request)
    con.commit()
    con.close()
    return ConversationHandler.END


def info(update, context):
    con = sqlite3.connect("Achievement.sqlite")
    cur = con.cursor()
    x = str(update.message.chat_id)
    request = f"""SELECT * from progress
    WHERE id = {x}"""
    res = cur.execute(request).fetchall()
    con.close()
    ans = list()
    ans.append("Game | Location | Difficulty | Points")
    for r in res:
        s = f"{r[1]} | {r[2]} | {r[3]} | {r[4]}"
        ans.append(s)
    update.message.reply_text('\n'.join(ans), reply_markup=help_markup)


def helper(update, context):
    update.message.reply_text(
        "Я - географический бот. Провожу викторины оп географии. Чтобы пройти викторину, нажми /start",
        reply_markup=help_markup)


def stop(update, context):
    update.message.reply_text("Извините за беспокойство, до свидания", reply_markup=help_markup)
    return ConversationHandler.END


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    continent_keyboard = [['Europe', 'Asia'], ['America', 'Africa']]
    continent_markup = ReplyKeyboardMarkup(continent_keyboard, one_time_keyboard=False)

    start_game_keyboard = [['Flags', 'Borders']]
    start_game_markup = ReplyKeyboardMarkup(start_game_keyboard, one_time_keyboard=False)

    difficulty_keyboard = [['Easy', 'Medium', 'Hard']]
    difficulty_markup = ReplyKeyboardMarkup(difficulty_keyboard, one_time_keyboard=False)

    beginning_keyboard = [['Начать']]
    beginning_markup = ReplyKeyboardMarkup(beginning_keyboard, one_time_keyboard=False)

    help_keyboard = [['/start', '/info', '/help']]
    help_markup = ReplyKeyboardMarkup(help_keyboard, one_time_keyboard=False)

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
            1: [MessageHandler(Filters.text & ~Filters.command, game_choice, pass_user_data=True)],
            2: [MessageHandler(Filters.text & ~Filters.command, continent_choice, pass_user_data=True)],
            3: [MessageHandler(Filters.text & ~Filters.command, diff_choice, pass_user_data=True)],
            "Borders1": [MessageHandler(Filters.text & ~Filters.command, border_quiz_1, pass_user_data=True)],
            "Borders2": [MessageHandler(Filters.text & ~Filters.command, border_quiz_2, pass_user_data=True)],
            "Borders3": [MessageHandler(Filters.text & ~Filters.command, border_quiz_3, pass_user_data=True)],
            # "Borders4": [MessageHandler(Filters.text & ~Filters.command, border_quiz_4, pass_user_data=True)],
            # "Borders5": [MessageHandler(Filters.text & ~Filters.command, border_quiz_5, pass_user_data=True)],
            # "Borders6": [MessageHandler(Filters.text & ~Filters.command, border_quiz_6, pass_user_data=True)],
            # "Borders7": [MessageHandler(Filters.text & ~Filters.command, border_quiz_7, pass_user_data=True)],
            # "Borders8": [MessageHandler(Filters.text & ~Filters.command, border_quiz_8, pass_user_data=True)],
            # "Borders9": [MessageHandler(Filters.text & ~Filters.command, border_quiz_9, pass_user_data=True)],
            # "Borders10": [MessageHandler(Filters.text & ~Filters.command, border_quiz_10, pass_user_data=True)],
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
            "Checkpoint": [MessageHandler(Filters.text & ~Filters.command, check_results, pass_user_data=True)],
            "SaveResults": [MessageHandler(Filters.text & ~Filters.command, save_results, pass_user_data=True)]
        },
        fallbacks=[MessageHandler(Filters.regex('/stop'), stop)]
    )
    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', helper))
    dp.add_handler(CommandHandler('login', login))
    # dp.add_handler(CommandHandler('reset', login))
    dp.add_handler(CommandHandler('info', info))
    # Регистрируем обработчик в диспетчере.
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()

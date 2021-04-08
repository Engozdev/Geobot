from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
import os
import sqlite3

TOKEN = "1629030108:AAFm4QIJw56pm0VXh5sLvu_3hcVQqioQyss"
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
    if ans.lower() not in ['flags', 'capitals', 'borders']:
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


def check_results(update, context):
    global user_answers
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
            update.message.reply_text(f"Wow, да ты географический гений! 10 из 10! Продолжай в том же духе!",
                                      reply_markup=help_markup)
        else:
            update.message.reply_text(f"Твой результат: {user_result} из 10. Неплохо, но ты можешь лучше",
                                      reply_markup=help_markup)
    return "SaveResults"
    # return ConversationHandler.END


def save_results(update, context):
    # Подключение к БД
    con = sqlite3.connect("Achievement.sqlite")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    request = f"""SELECT * FROM progress
WHERE id = {update.message.chat_id}"""
    result = cur.execute(request).fetchall()
    if not request:
        print('Empty')
    else:
        cur.execute(
            f"""INSERT INTO process VALUES ({update.message.chat_id}, {context.user_data["game"]}, {context.user_data["continent"]}, {context.user_data["difficulty"]})""")
        result = cur.execute(request).fetchall()
    print(result)


def stop(update, context):
    update.message.reply_text("Извините за беспокойство, до свидания")
    return ConversationHandler.END


def helper(update, context):
    update.message.reply_text(
        "Я - географический бот. Провожу викторины оп географии. Чтобы пройти викторину, нажми /start",
        reply_markup=help_markup)


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    continent_keyboard = [['Europe', 'Asia', 'Africa'], ['South America', 'Northern America']]
    continent_markup = ReplyKeyboardMarkup(continent_keyboard, one_time_keyboard=False)

    start_game_keyboard = [['Flags', 'Borders']]
    start_game_markup = ReplyKeyboardMarkup(start_game_keyboard, one_time_keyboard=False)

    difficulty_keyboard = [['Easy', 'Medium', 'Hard']]
    difficulty_markup = ReplyKeyboardMarkup(difficulty_keyboard, one_time_keyboard=False)

    beginning_keyboard = [['Начать']]
    beginning_markup = ReplyKeyboardMarkup(beginning_keyboard, one_time_keyboard=False)

    help_keyboard = [['/start']]
    help_markup = ReplyKeyboardMarkup(help_keyboard, one_time_keyboard=False)
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

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
        fallbacks=[MessageHandler(Filters.command, stop)]
    )
    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', helper))
    # Регистрируем обработчик в диспетчере.
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()

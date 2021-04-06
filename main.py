from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler

TOKEN = "TOKEN"


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.


def start(update, context):
    s = "Привет, я бот-географ. Я люблю проводить викторину, географические конечно.\nДавай сыграем! Выбери викторину:"
    update.message.reply_text(
        s,
        reply_markup=start_game_markup
    )
    return 1


def game_choice(update, context):
    ans = update.message.text
    context.user_data['game'] = ans
    update.message.reply_text("Теперь выбери континент:", reply_markup=continent_markup)
    return ConversationHandler.END


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

    start_game_keyboard = [['Flags', 'Capitals', 'Borders']]
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
        states={},
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

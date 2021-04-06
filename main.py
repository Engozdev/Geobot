from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram import ReplyKeyboardMarkup

TOKEN = "TOKEN"


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text(update.message.text)


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
    text_handler = MessageHandler(Filters.text, echo)

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(text_handler)
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()

# kittybot/kittybot.py

from telegram.ext import CommandHandler, Updater, Filters, MessageHandler
from telegram import ReplyKeyboardMarkup

updater = Updater(token='6925824860:AAEQiG0l3P0MtuFXo1xPiSC3VT6UpfwHQOw')

def say_hi(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    # В ответ на любое текстовое сообщение 
    # будет отправлено 'Привет, я KittyBot!'
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    # В ответ на команду /start 
    # будет отправлено сообщение 'Спасибо, что включили меня'
    name = update.message.chat.first_name
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([
            ['Который час?', 'Определи мой ip'],
            ['/random_digit']
        ])
    context.bot.send_message(chat_id=chat.id, 
                             text='Спасибо, что вы включили меня, {}!'.format(name),
                             reply_markup=buttons)

# Регистрируется обработчик CommandHandler;
# он будет отфильтровывать только сообщения с содержимым '/start'
# и передавать их в функцию wake_up()
updater.dispatcher.add_handler(CommandHandler('start', wake_up))

# Регистрируется обработчик MessageHandler;
# из всех полученных сообщений он будет выбирать только текстовые сообщения
# и передавать их в функцию say_hi()
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

# Метод start_polling() запускает процесс polling, 
# приложение начнёт отправлять регулярные запросы для получения обновлений.
updater.start_polling(poll_interval=10.0)
# Бот будет работать до тех пор, пока не нажмете Ctrl-C
updater.idle()
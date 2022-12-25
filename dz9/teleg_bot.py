from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5407023438:AAF3fXfzZe1vhdm8xjpSsyWTzUqUb6cK5UA')
updater = Updater(token='5407023438:AAF3fXfzZe1vhdm8xjpSsyWTzUqUb6cK5UA')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет, я бот, могу удалить "абв" из сообщения')

def deleted(update, context):
    text = update.message.text
    if 'абв' in text:
        s = [i for i in text.split() if 'абв' not in i]
        context.bot.send_message(update.effective_chat.id, ' '.join(s))
    else:
        context.bot.send_message(update.effective_chat.id, 'в этом сообщении нет "абв"')


start_handler = CommandHandler('start', start)
deleted_handler = MessageHandler(Filters.text, deleted)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(deleted_handler)

updater.start_polling()
updater.idle()
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd

# TOKEN = '5407023438:AAF3fXfzZe1vhdm8xjpSsyWTzUqUb6cK5UA'
bot = Bot(token='5407023438:AAF3fXfzZe1vhdm8xjpSsyWTzUqUb6cK5UA')
updater = Updater(token='5407023438:AAF3fXfzZe1vhdm8xjpSsyWTzUqUb6cK5UA')
dispatcher = updater.dispatcher

A = 0
B = 1


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет. Как у вас дела?")
    return A

def howareyou(update, context):
    text = update.message.text
    if 'хор' in text.lower():
        context.bot.send_message(update.effective_chat.id, "Я рад что у тебя все хорошо")
    else:
        context.bot.send_message(update.effective_chat.id, "Не грусти, все будет отлично")
    context.bot.send_message(update.effective_chat.id, "Как погода?")
    return B

def wether(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, "И у меня такая же погода")
    return ConversationHandler.END

# def rand(update, context):
#     context.bot.send_message(update.effective_chat.id, f'{rd(1,100)}')

# def func(update, context):
#     text = update.message.text
#     if 'прив' in text.lower():
#         context.bot.send_message(update.effective_chat.id,"И тебе привет, мой дорогой друг!")
#     else:
#         context.bot.send_message(update.effective_chat.id,"Я тебя не понимаю ;")

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, "Прощай")


start_handler = CommandHandler('start', start)
howareyou_handler = MessageHandler(Filters.text, howareyou)
wether_handler = MessageHandler(Filters.text, wether)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={A: [howareyou_handler],
                                    B: [wether_handler]},
                                    fallbacks=[cancel_handler]
                                    )

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(start_handler)
# dispatcher.add_handler(random_handler)
# dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()

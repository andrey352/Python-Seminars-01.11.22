# Создать калькулятор для работы с рациональными, организовать меню, добавив в неё
#  систему логирования(Содержит: id.Пользователь, ввод, результат)

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


#TOKEN = "5407023438:AAF3fXfzZe1vhdm8xjpSsyWTzUqUb6cK5UA"
bot = Bot(token='5407023438:AAF3fXfzZe1vhdm8xjpSsyWTzUqUb6cK5UA')
updater = Updater(token='5407023438:AAF3fXfzZe1vhdm8xjpSsyWTzUqUb6cK5UA')
dispatcher = updater.dispatcher

result = 0
sent = ''

A = 0
B = 1

def start(update, context):
    context.bot.send_message(update.effective_chat.id,"Привет\nКак Вас зовут?")
    return A

def get_name(update, context):
    global name
    name = update.message.text
    context.bot.send_message(update.effective_chat.id,f"Ок {name}. Что нужно подсчитать? Введите без пробелов")
    return B

def calc(update, context):
    sent = update.message.text 
    s = [i for i in sent.split()]
    print(s)
    components = [int(i) if i.isdigit() else i for i in sent]
    print(components)
    while '*' in components:
        i = components.index('*')
        result = components[i - 1] * components[i + 1]
        components = components[:i - 1] + [result] + components[i + 2:]
    while '/' in components:
        i = components.index('/')
        result = components[i - 1] / components[i + 1]
        components = components[:i - 1] + [result] + components[i + 2:]
    while '+' in components:
        i = components.index('+')
        result = components[i - 1] + components[i + 1]
        components = components[:i - 1] + [result] + components[i + 2:]
    while '-' in components:
        i = components.index('-')
        result = components[i - 1] - components[i + 1]
        components = components[:i - 1] + [result] + components[i + 2:]
    print(components)
    print(result)
    context.bot.send_message(update.effective_chat.id, result)

    with open('file.txt', 'a') as data:
        rec = name + " " + sent + " = " + str(result) + ";\n"
        data.writelines(rec)
        print(rec)
        print(name)
    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, "Прощай")


start_handler = CommandHandler('start', start)
get_name_handler = MessageHandler(Filters.text, get_name)
calc_handler = MessageHandler(Filters.text, calc)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={A: [get_name_handler],
                                    B: [calc_handler]},
                                    fallbacks=[cancel_handler]
                                    )

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()

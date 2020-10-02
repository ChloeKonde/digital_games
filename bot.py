import logging, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup


updater = Updater(token='', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Я эко-бот Капля💧\nДавай я тебе расскажу, что я умею, но не забудь указать свою геопозицию🌏\n🔹Определю степень загрязнения воздуха в указанной тобой местности;\n🔹Покажу ближайшие пункты переработки вторсырья;\n🔹Расскажу, где находятся места, предоставляющие услугу Traid in;\n🔹Поделюсь информацией о предстоящих акциях, в которых ты можешь принять участие и помочь экологии\n", reply_markup=start_menu())


def start_menu():
    points = KeyboardButton(text='Пункты приёма вторсырья')
    traid_in = KeyboardButton(text='Traid in')
    volunteering = KeyboardButton(text='Волонтёрство')
    air_state = KeyboardButton(text='Состояние воздуха')
    return ReplyKeyboardMarkup([[points, traid_in], [volunteering, air_state]], resize_keyboard=True)


def second_menu():
    paper = KeyboardButton(text='Бумага')
    plastic = KeyboardButton(text='Пластик')
    glass = KeyboardButton(text='Стекло')
    steel = KeyboardButton(text='Железо')
    wears = KeyboardButton(text='Одежда')
    alls = KeyboardButton(text='Всё и сразу')
    back = KeyboardButton(text='Назад')
    return ReplyKeyboardMarkup([[alls, paper], [glass, plastic], [wears, steel, back]], resize_keyboard=True)


def back_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Выберите пункт(?)", reply_markup=start_menu())


def points_handler(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Что желаете сдать?", reply_markup=second_menu())


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.regex('Назад'), back_handler))
dispatcher.add_handler(MessageHandler(Filters.regex('Пункты приёма вторсырья'), points_handler))
updater.start_polling()

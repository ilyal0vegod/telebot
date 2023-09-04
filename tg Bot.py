import telebot
from telebot import types

bot = telebot.TeleBot('6617866210:AAFxwHaAahZvkt0aXbLUkb_0Slv2obHdZq0')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🤑Получить скидку 10%")
    btn2 = types.KeyboardButton('Открыть доступ🔐')
    btn3 = types.KeyboardButton('🔧Тех поддержка')
    btn4 = types.KeyboardButton('Реферальная система✅')
    btn5 = types.KeyboardButton('Вернуться на канал☺️')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, "Привет, вот что я могу предложить.", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '🤑Получить скидку 10%':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Извините, сегодня бесплатные промокоды закончились☹️', reply_markup=markup)
    if message.text == 'Открыть доступ🔐':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Нужно произвести оплату через СБП по номеру телефона +79933230844(Тинькофф) на сумму 99 рублей. Важно❗️❗️❗️ Сумма должна быть = 99,00 руб, иначе система не посчитает оплату. После оплаты в течении 15 минут будет выдана ссылка приглашение в закрытый чат.', reply_markup=markup)
    if message.text == '🔧Тех поддержка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'https://t.me/Ilyusha_lnvest', reply_markup=markup)
    if message.text == 'Реферальная система✅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Ваш персональный промокод: Skuns. Поделитесь им с друзьями.', reply_markup=markup)
    if message.text == 'Skuns':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Извините, реферальная система еще в разработке.', reply_markup=markup)
    if message.text == 'Вернуться на канал☺️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'https://t.me/Ilya_lnvest', reply_markup=markup)




bot.polling(none_stop=True)
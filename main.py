import telebot

from telebot import types

bot = telebot.TeleBot("905266572:AAF0hAMoP01I2Vx-diR7_mgyhFw0NT4XWHI")



@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Поговорим?")
    item2 = types.KeyboardButton("Сыграем?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть твоим другом."
                    .format(message.from_user, bot.get_me()),
                    parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'Сыграем?':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item5 = types.InlineKeyboardButton("Давай", callback_data='yes1')

        markup.add(item5)

        bot.send_message(message.chat.id, 'Сыграем?', reply_markup=markup)


    if message.text == "сахар":
        bot.send_message(message.chat.id, 'Молодец, правильно')
    if message.chat.type == 'private':
        if message.text == 'Поговорим?':
            bot.send_message(message.chat.id, "Привет")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item4 = types.InlineKeyboardButton("Плохо", callback_data='bad')

            markup.add(item3, item4)

            bot.send_message(message.chat.id, 'Как дела?', reply_markup=markup)


        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            try:
                if call.message:
                    if call.data == 'good':
                        bot.send_message(call.message.chat.id, 'Вот и отличненько')
                    if call.data == 'bad':
                        bot.send_message(call.message.chat.id, 'Держи, не грусти 🎂')
                if call.message:
                    if call.data == 'yes1':
                        bot.send_message(call.message.chat.id,
                                         'Отгадай загадку, Белый снег есть у всех, в рот попадает в миг пропадает')



            except Exception as e:
                print(repr(e))


# RUN
bot.polling(none_stop=True)
bot.polling(none_stop=True)

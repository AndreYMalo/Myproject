import telebot
bot = telebot.TeleBot("905266572:AAF0hAMoP01I2Vx-diR7_mgyhFw0NT4XWHI")
# bot.send_message(1149221538, "Hello")

# upd = bot.get_updates()
# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)

#print(bot.get_me())
#def log(message, answer):
   # print('\n ------')
   # from datetime import datetime
    #print(datetime.now())
    #print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   #message.from_user.last_name,
                                                                   #str(message.from_user.id),
                                                                   #message.text))

#print(answear)

@bot.message_handler(commands=["start"])
def handler_start(message):
     user_markup = telebot.types.ReplyKeyboardMarkup()
     user_markup.row("/start","/stop")
     user_markup.row("fsdfag", "photo")
     user_markup.row("music", "video")
     bot.send_message(message.from_user.id, "Выбирай!",reply_markup=user_markup)
#
#
#
#
# #    print("ПРИШЛО СООБЩЕНИЕ ОМАГАД")
bot.polling(none_stop=True, interval=0)

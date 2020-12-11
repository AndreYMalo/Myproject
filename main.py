import COVID19Py
from telebot import types
import telebot

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1453562215:AAEzET3P8qhTpWM9E7Zz-cFFq-SAKBzCXUs')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('Во всём мире')
    item2 = types.KeyboardButton('Украина')
    item3 = types.KeyboardButton('Россия')
    item4 = types.KeyboardButton('Беларусь')
    item5 = types.KeyboardButton('Италия')
    item7 = types.KeyboardButton('Франция')
    item8 = types.KeyboardButton('Германия')
    item9 = types.KeyboardButton('Япония')
    item10 = types.KeyboardButton('США')
    item11 = types.KeyboardButton('Турция')
    markup.add(item1, item2, item3, item4, item5, item7, item8, item9, item10, item11)

    send_message = f"<b>Пиривет, {message.from_user.first_name}!</b>\nХочешь узнать статистику по короне, тогда напиши " \
                   f"название страны, например: США, Украина, Россия и так далее."

    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
        photo = open('C:\Flagi/США.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
        photo = open('C:\Flagi/Украина.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
        photo = open('C:\Flagi/Россия.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode("BY")
        photo = open('C:\Flagi/www.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
        photo = open('C:\Flagi/Италия.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode("FR")
        photo = open('C:\Flagi/Франция.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode("DE")
        photo = open('C:\Flagi/Германия.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif get_message_bot == "япония":
        location = covid19.getLocationByCountryCode("JP")
        photo = open('C:\Flagi/Япония.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif get_message_bot == "турция":
        location = covid19.getLocationByCountryCode("TR")
        photo = open('C:\Flagi/Турция.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заразились короной: </b>{location['confirmed']:,}\n<b>Погибло: </b>{location['deaths']:,}"


    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nЖивёт в стране: {location[0]['country_population']:,}\n" \
                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние новости:\n<b>" \
                        f"Заразились короной: </b>{location[0]['latest']['confirmed']:,}\n<b>Погибло: </b>" \
                        f"{location[0]['latest']['deaths']:,}"


    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)

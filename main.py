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
    item5 = types.KeyboardButton('Казахстан')
    item6 = types.KeyboardButton('Италия')
    item7 = types.KeyboardButton('Франция')
    item8 = types.KeyboardButton('Германия')
    item9 = types.KeyboardButton('Япония')
    item10 = types.KeyboardButton('Китай')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

    send_message = f"<b>Привет, {message.from_user.first_name}!</b>\nЧтобы узнать данные по коронавирусу напишите " \
                   f"название страны, например: США, Украина, Россия и так далее."
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "казакхстан":
        location = covid19.getLocationByCountryCode("KZ")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "япония":
        location = covid19.getLocationByCountryCode("JP")
    elif get_message_bot == "китай":
        location = covid19.getLocationByCountryCode("CN")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевшие: </b>{location['confirmed']}\n"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)

import telebot
from config import value_key, TOKEN
from extensions import APIException, Convertor

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = 'Для начала работы введите боту команду в формате: \
\n<имя валюты> <валюта перевода> <кол.во перевдимой валюты>'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for curr in value_key.keys():
        text = '\n'.join((text, curr, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Неверное количество параметров!')

        answer = Convertor.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f'Ошибка в команде!')
    except Exception as e:
        bot.reply_to(message, 'Неизвестная ошибка!')
    else:
        bot.reply_to(message, answer)

bot.polling()
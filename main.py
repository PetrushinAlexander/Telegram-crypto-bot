from importlib.metadata import requires
from urllib import response
import requests
from datetime import datetime
from auth_data import token
import telebot


def get_data():
    req= requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()
    sell_price = response['btc_usd']['sell']
    print( f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n Sell BTC price: {sell_price}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id,"Добро пожаловать!\n Напишите 'цена' для того, чтобы узнать цену биткоина")
        
    @bot.message_handler(content_types = ['text'])
    def send_text(message):
        if message.text.lower() =="цена":
            try:
                req= requests.get('https://yobit.net/api/3/ticker/btc_usd')
                response = req.json()
                sell_price = response['btc_usd']['sell']
                bot.send_message(
                    message.chat.id,
                    ( f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n Sell BTC price: {sell_price}")
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Хмм..Что-то пошло не так.."
                    )
        
        else:
            bot.send_message(message.chat.id,"Неизвестная команда, попробуйте еще раз")


    bot.infinity_polling()



if __name__ == '__main__':
    telegram_bot(token)
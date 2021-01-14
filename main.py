import config
import telebot
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://sinoptik.ua/погода-краснодар')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot('1536872083:AAFm_xHvohB_IPBJ3COnn3MTrH3lPqIydk4')

for el in html.select('#content'):
    t_min = el.select('.temperature .min') [0].text
    t_max = el.select('.temperature .max') [0].text
    text = el.select('.wDescription .description')[0].text

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Надеюсь, ты готов к новому дню. Могу помочь с этим!")

@bot.message_handler(commands=['command1'])
def main(message):
	bot.send_message(message.chat.id, "Привет, погода на сегодня в твоём любимом городе:\n" +
        t_min + ', ' + t_max + '\n' + text    )

@bot.message_handler(commands=['command2'])
def main(message):
	bot.send_message(message.chat.id, "Проверим, что происходит на дороге:" '\n' "http://краснодар.пробки-онлайн.рф/"  )

@bot.message_handler(commands=['command3'])
def main(message):
	bot.send_message(message.chat.id, "Может сегодня проходит концерт на который ты хочешь сходить?" '\n' 'https://krd.kassir.ru/')

@bot.message_handler(commands=['command4'])
def main(message):
	bot.send_message(message.chat.id, "Прочти новости, прежде чем выйти из дома:https://kubnews.ru/")

@bot.message_handler(commands=['command5'])
def main(message):
	bot.send_message(message.chat.id, "Если ты турист, то рекомендую следующую подборку мест: https://tripplanet.ru/dostoprimechatelnosti-krasnodara/")

@bot.message_handler(commands=['command5'])
def main(message):
	bot.send_message(message.chat.id, "Если ты турист, то рекомендую следующую подборку мест: https://tripplanet.ru/dostoprimechatelnosti-krasnodara/")

@bot.message_handler(commands=['command6'])
def main(message):
	bot.send_message(message.chat.id,'Кстати, повод остаться дома covid-ситуация:https://coronavirus-monitor.info/' )

@bot.message_handler(commands=['stop'])
def main(message):
	bot.send_message(message.chat.id, "Если ты так и не решился выйти из дома, то закажи пиццу:https://www.papajohns.ru/krasnodar?code=0123&utm_source=yandex&utm_medium=cpc_search&utm_term=заказать%20пиццу&utm_content=7014822642&utm_campaign=krasnodar_pizza_search_y&yclid=18303836735438611034 ")

if __name__ == '__main__':
    bot.polling(none_stop=True)

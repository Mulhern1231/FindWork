import requests
from bs4 import BeautifulSoup
import telebot
import os

def habr():
    url = 'https://freelance.habr.com/tasks?q=%5Bpython%E2%80%8B%5D?q=%5Bpython%E2%80%8B%5D'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    task = soup.find_all('div', class_='task__title')
    responses = soup.find_all('div', class_='task__params')
    list_habr = []
    for i in range(len(task)):
        list_habr.append(task[i].text + "\n" + responses[i].text + "\n" + "https://freelance.habr.com" + soup.select(f'#tasks_list > li:nth-child({i+1}) > article > div > header > div.task__title > a')[0].get('href'))
    return list_habr[::-1]

def fl():
    url = 'https://www.fl.ru/search/?action=search&type=projects&search_string=python'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    task = soup.find_all('div', class_='search-lenta-item')
    
    list_fl = []
    for i in range(len(task)):
        list_fl.append(soup.select(f'#search-lenta > div:nth-child({i+1}) > div > h3')[0].text + "\n" + soup.select(f'#search-lenta > div:nth-child({i+1}) > div > p')[0].text.replace(' ... ','') + "\n" + "https://www.fl.ru" + soup.select(f'#search-lenta > div:nth-child({i+1}) > div > h3 > a')[0].get('href'))
    return list_fl[::-1]

token = "5262384131:AAFD2_JdieEHWPOlaSOfcwOR2JJQN6Cg0P4"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, "Привет! Сюда будут приходить заказы с фриланс сайтов для языка Python")

@bot.message_handler(content_types=['text'], commands=["ID"])
def habrTG(message):
    bot.send_message(message.from_user.id, message.from_user.id )

@bot.message_handler(content_types=['text'], commands=["habr"])
def habrTG(message):
    if str(message.from_user.id) == "426156432":
        for i in habr()[0:3]:
            bot.send_message(message.from_user.id, i )
    else:
        bot.send_message(message.from_user.id, "НЕРАСПОЗНАН :(")

@bot.message_handler(content_types=['text'], commands=["fl"])
def flTG(message):
    if str(message.from_user.id) == "426156432":
        for i in fl()[0:3]:
            bot.send_message(message.from_user.id, i )
    else:
        bot.send_message(message.from_user.id, "НЕРАСПОЗНАН :(")

bot.polling(none_stop=True, interval=0)

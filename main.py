import requests
from bs4 import BeautifulSoup


def Habr():
    url = 'https://freelance.habr.com/tasks?q=%5Bpython%E2%80%8B%5D?q=%5Bpython%E2%80%8B%5D'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    task = soup.find_all('div', class_='task__title')
    responses = soup.find_all('div', class_='task__params')
    list_habr = []
    for i in range(len(task)):
        list_habr.append(task[i].text + "\n" + responses[i].text + "\n" + "https://freelance.habr.com" + soup.select(f'#tasks_list > li:nth-child({i+1}) > article > div > header > div.task__title > a')[0].get('href'))
    return list_habr.reverse()

def fl():
    url = 'https://www.fl.ru/search/?action=search&type=projects&search_string=python'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    task = soup.find_all('div', class_='search-lenta-item')
    
    list_fl = []
    for i in range(len(task)):
        list_fl.append(soup.select(f'#search-lenta > div:nth-child({i+1}) > div > h3')[0].text + "\n" + soup.select(f'#search-lenta > div:nth-child({i+1}) > div > p')[0].text.replace(' ... ','') + "\n" + "https://www.fl.ru" + soup.select(f'#search-lenta > div:nth-child({i+1}) > div > h3 > a')[0].get('href'))
    return list_fl.reverse()

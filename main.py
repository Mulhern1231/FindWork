import requests
from bs4 import BeautifulSoup

url = 'https://freelance.habr.com/tasks?q=%5Bpython%E2%80%8B%5D?q=%5Bpython%E2%80%8B%5D'



response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

task = soup.find_all('div', class_='task__title')
responses = soup.find_all('div', class_='task__params')
list_habr = []
for i in range(len(task)):
    list_habr.append(task[i].text + "\n" + responses[i].text + "\n" + "https://freelance.habr.com" + soup.select(f'#tasks_list > li:nth-child({i+1}) > article > div > header > div.task__title > a')[0].get('href'))
    

list_habr.reverse()
for text in list_habr:
    print(text)
    print("__________")

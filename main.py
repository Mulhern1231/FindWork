import requests
from bs4 import BeautifulSoup

url = 'https://freelance.habr.com/tasks?q=%5Bpython%E2%80%8B%5D?q=%5Bpython%E2%80%8B%5D'



response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


task = soup.find_all('div', class_='task__title')
responses = soup.find_all('div', class_='task__params')

for i in range(len(task)):
    print(task[i].text)
    print(responses[i].text)
    print("\n")
    


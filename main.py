from pprint import pprint
import requests
from operator import itemgetter, attrgetter, methodcaller

TOKEN = "2619421814940190"


class SuperHero():
    def __init__(self, name):
        self.name = name
        self.id = get_id(self.name)
        self.intelligence = int(get_intelligence(self.id))

    def __str__(self):
        return f'{self.name} id: {self.id}, обладает интеллектом: {self.intelligence}'

    def __lt__(self, other):
        return self.intelligence > other.intelligence


def get_id(name):
    url = f'https://www.superheroapi.com/api.php/{TOKEN}/search/{name}'
    response = requests.get(url)
    id = response.json()
    check_box = 0  # переменная для отслеживания совпадения имени персонажа
    for i in id['results']:
        if name == i['name']:
            check_box_found = check_box  # присваивание индекса найденного персонажа
        check_box += 1
    return id['results'][check_box_found]['id']


def get_intelligence(id):
    url = f"https://www.superheroapi.com/api.php/{TOKEN}/{id}/powerstats/"
    response = requests.get(url)
    dict = response.json()['intelligence']
    return dict


cap = SuperHero('Captain America')
thanos = SuperHero("Thanos")
hulk = SuperHero('Hulk')

raw_list = [cap, thanos, hulk]


def sort_list(raw):
    finish_list = sorted(raw, key=attrgetter('intelligence'), reverse=True)
    print('Рейтинг интеллекта по убыванию:')
    for i in finish_list:
        print(i)


if __name__ == '__main__':
    sort_list(raw_list)

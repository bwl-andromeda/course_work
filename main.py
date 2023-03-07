import requests
from pprint import pprint
from TOKEN import TOKEN
import json


def get_req(id): # Данной функцией мы реализуем запрос на VK_API и вытаскиваем фотки в json формате в файл который мы можем дальше обрабатывать
    url = "https://api.vk.com/method/photos.get"
    req = requests.get(f'{url}?owner_id={id}&album_id=profile&rev=0&extended=1&count=100&access_token={TOKEN}&v=5.131').json()
    with open("file.json",'w') as file:
        json.dump(req, file, indent=4)

def init_file():

    with open ("file.json") as file:
        new_file = json.load(file)

        new_dict = {}
        data = new_file["response"]["items"]

        for i in data:
            for j in i["sizes"]:
                pass
             

            
        


if __name__ == "__main__":
    get_req(236801795)
    init_file()

# Хм... Я реализовал 1 пункт - (Получать фотографии с профиля. Для этого нужно использовать метод photos.get.)
# Нужно теперь продумать логику как я буду - сохранять фотографии максимального размера(ширина/высота в пикселях) на Я.Диске.
# Пытаюсь вытащить из json все что нужно... пока что безуспешно... пойду лучше лягу спать(1:03)



# #Входные данные:
# Пользователь вводит:

# id пользователя vk; - accept!
# токен с Полигона Яндекс.Диска. Важно: Токен публиковать в github не нужно!    
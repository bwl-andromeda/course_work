import requests
from TOKEN import TOKEN
from datetime import datetime
import os
import yadisk
from tqdm import tqdm
import time
import shutil

def get_req():
    print("Введите пожалуйста ваш айди:")
    id = int(input())
    print("-" * 100)
    url = "https://api.vk.com/method/photos.get"
    req = requests.get(f'{url}?owner_id={id}&album_id=profile&rev=0&extended=1&count=100&access_token={TOKEN}&v=5.131').json()

    str_photos = "wzyrqpoxms"
    new_dict = {}
    list = req["response"]["items"]

    print("Создание словаря...")
    print("-" * 100)
    for photo in tqdm(list):
        time.sleep(0.1)
        if photo['likes']['count'] not in new_dict.keys():
            file_name = photo['likes']['count']
        else:
            file_name = f"{photo['likes']['count']}_date_{(datetime.utcfromtimestamp(photo['date']).strftime('%d-%m-%Y_%H-%M-%S'))}"

        max_size = 0


        for size in photo["sizes"]:
            counter = 9
            if size["height"] > 0:
                if size["height"] > max_size:
                    new_dict[file_name] = {'url':size['url'],'type':size['type']}
                    max_size = size["height"]
            else:
                if str_photos.index(size["type"]) < counter:
                    new_dict[file_name] = {'url':size['url'],'type':size['type']}
                    counter = str_photos.index(size["type"])
    
    
    print("Создание папки для фоток.")
    os.mkdir("vk_photo")
    print("-" * 100)
    print("Выгрузка фото на файл на ПК")
    print("-" * 100)
    for i in tqdm(new_dict):
        time.sleep(0.1)
        url = new_dict[i]["url"]
        r = requests.get(url,stream=True)
        with open(f"vk_photo\{i}.jpg",'wb') as new_file:
            for new in r.iter_content(chunk_size=4096*50):
                    new_file.write(new)


    print("Фотки были успешно загружены на ПК")
    print("-" * 100)



def upload_photo():
    print('Введите пожалуйста ваш токен: ')
    TOKEN_YANDEX = input()
    print("-" * 100)
    path = r'C:\Users\Tekila\Desktop\repository\course_work\vk_photo'
    uploader = yadisk.YaDisk(token = TOKEN_YANDEX)
    print("Введите название папки:")
    name = input()
    uploader.mkdir(name)
    count = 0
    for address, dirs, files in os.walk(path):
        for file in tqdm(files):
            time.sleep(0.1)
            if count < 10:
                print()
                uploader.upload(f'{address}/{file}', f'/{name}/{file}')
                print(f'Файл {file} загружен')
                print("-" * 100)
                count +=1
    print("Очистка кеша...")
    print("-" * 100)
    shutil.rmtree("vk_photo")
    print("-" * 100)
    print("Программа завершена...")

if __name__ == "__main__":
    get_req()
    upload_photo()
import requests
import os
from datetime import datetime
import json


class ApiYaDisk:
    BASE_URL = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str) -> None:
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
            }

    def upload_photo(self, photos: dict, path_folder: str) -> list:
        self.__create_folder(path_folder)
        photo_info = []
        for url_photo, name in self.__create_names(photos).items():
            bytes_photo = requests.get(url_photo).content
            response = requests.put(self.__get_href_upload(f'{path_folder}/{name}'), data=bytes_photo)
            if response.status_code == 201:
                photo_info.append({
                    "file_name": name,
                    "size": len(bytes_photo)
                    })
                print(f'Фото {name} загружено ({response.status_code})')
            else:
                print(f'Фото {name} не загружено ({response.status_code})')
        self.__write_photo_info(photo_info)
        return photo_info

    def __get_href_upload(self, path: str) -> str:
        url = f'{self.BASE_URL}v1/disk/resources/upload'
        params = {
            'path': path, 
            'overwrite': 'true'
            }
        return requests.get(url, headers=self.headers, params=params).json()['href']

    def __create_folder(self, path: str) -> bool:
        url = f'{self.BASE_URL}v1/disk/resources'
        params = {"path": path}
        response = requests.put(url,headers=self.headers, params=params)
        return response.status_code == 201 or response.status_code == 409
    
    def __create_names(self, photos: dict) -> dict:
        rename_photos = {}
        for url, likes  in photos.items():
            if list(photos.values()).count(likes) == 1:
                rename_photos[url] = f'{likes}.jpg'
            else:
               rename_photos[url] = f'{likes}{datetime.now}.jpg' 
        return rename_photos
    
    def __write_photo_info(self, photo_info: list[dict]) -> None:
         with open('photoInfo.txt', 'w') as f:
            f.write(json.dumps(photo_info, indent=1))


    


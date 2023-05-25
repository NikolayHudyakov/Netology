import requests
from datetime import datetime
import json
from tqdm import tqdm


class ApiYaDisk:
    BASE_URL = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str) -> None:
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
            }

    def upload_photo(self, photos: dict, path_folder: str) -> list[dict]:
        self.__create_folder(path_folder)
        url = f'{self.BASE_URL}v1/disk/resources/upload'
        photo_info = []
        for url_photo, data in tqdm(self.__create_names(photos).items()):
            params = {
            'path': f'{path_folder}/{data["name"]}', 
            'url': url_photo
            }
            response = requests.post(url, headers=self.headers, params=params)
            if response.status_code == 202 and 'error' not in response.json():
                photo_info.append({
                    "file_name": data["name"],
                    "size": data["size_type"]
                    })
        self.__write_photo_info(photo_info)
        return photo_info

    def __create_folder(self, path: str) -> bool:
        url = f'{self.BASE_URL}v1/disk/resources'
        params = {"path": path}
        response = requests.put(url,headers=self.headers, params=params)
        return response.status_code == 201 or response.status_code == 409
    
    def __create_names(self, photos: dict) -> dict:
        rename_photos = {}
        for url, data in photos.items():
            if list(map(lambda ls: ls['likes'], photos.values())).count(data['likes']) == 1:
                name = f'{data["likes"]}.jpg'
            else:
                name = f'{data["likes"]}{datetime.now}.jpg'
            rename_photos[url] = {
                    'name': name,
                    'size_type': data['size_type']
                    }
        return rename_photos
    
    def __write_photo_info(self, photo_info: list[dict]) -> None:
         with open('photoInfo.json', 'w') as f:
            f.write(json.dumps(photo_info, indent=1))


    


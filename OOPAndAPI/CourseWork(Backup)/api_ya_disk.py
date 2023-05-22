import requests
import os


class ApiYaDisk:
    def __init__(self, token: str) -> None:
        self.token = token

    def upload_photo(self, photos: list[dict], path_folder: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
            }
        for photo in photos:
            params = {
                "path": f'/{path_folder}/{str(photo["likes"])}.jpg', 
                "overwrite": "true"
                }
            href = requests.get(url, headers=headers, params=params).json()['href']
            bytes_photo = requests.get(photo['url']).content
            response = requests.put(href, data=bytes_photo)
            print(response.status_code)
            yield response.status_code == 201

    # def __create_folder(self, path: str) -> bool:
    #     url = 'https://cloud-api.yandex.net/v1/disk/resources'
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'Authorization': f'OAuth {self.token}'
    #         }
    #     params = {"path": path}
    #     response = requests.put(url, params=params)
    #     return response.status_code == 201

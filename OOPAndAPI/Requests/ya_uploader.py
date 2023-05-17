import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str) -> bool:
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {"path": 'test', "overwrite": "true"}
        href = requests.get(upload_url, headers=headers, params=params).json()['href']
        print(href)
        response = requests.put(href, data=open(file_path, 'rb'))
        return response.status_code == 201

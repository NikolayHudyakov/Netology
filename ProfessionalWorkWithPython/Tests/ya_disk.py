import requests
from requests.compat import urljoin


class YaDisk:
    BASE_URL = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str) -> None:
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
        }

    def create_folder(self, path: str) -> int:
        url = urljoin(self.BASE_URL, 'v1/disk/resources')
        params = {"path": path}
        response = requests.put(url, headers=self.headers, params=params)
        return response.status_code

import requests


class ApiVK:
    def __init__(self, token: str, version='5.131') -> None:
        self.params = {'access_token': token, 'v': version}

    def get_url_user_photos(self, owner_id: int) -> list[dict]:
        url = f'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': owner_id, 
            'album_id': 'profile', 
            'extended': 1, 
            **self.params
            }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data_photos = response.json()['response']['items']
            return list(map(lambda p: {
                                'likes': p['likes']['count'], 
                                'url': self.__get_url_maxsize_photo(p['sizes'])
                                }, 
                            data_photos))
        return response.status_code
    
    def __get_url_maxsize_photo(self, photos: list[dict]) -> str:
        return max(photos, key=lambda p: p['height'] * p['width'])['url']
    

    

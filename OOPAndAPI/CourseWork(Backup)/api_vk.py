import requests
import os


class ApiVK:
    def __init__(self, version='5.131') -> None:
        self.params = {
            'access_token': os.getenv('VK_API_TOKEN'), 
            'v': version
            }

    def get_url_user_photos(self, owner_id: int, quantity=5) -> dict:
        url = f'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': owner_id, 
            'album_id': 'profile', 
            'extended': 1, 
            'count': quantity,
            **self.params
            }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data_photos = response.json()['response']['items']
            photos = {}
            for photo in data_photos:
                max_size_photo = self.__get_url_maxsize_photo(photo['sizes'])
                photos[max_size_photo['url']] = {
                    'likes': photo['likes']['count'],
                    'size_type': max_size_photo['type']
                    } 
            return photos
        return response.status_code
    
    def __get_url_maxsize_photo(self, photos: list[dict]) -> dict:
        return max(photos, key=lambda p: p['height'] * p['width'])
    

    

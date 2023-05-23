import os
from dotenv import load_dotenv
from pprint import pprint

from api_vk import ApiVK
from api_ya_disk import ApiYaDisk

class Backup:
    def __init__(self,  ya_disk_token: str) -> None:
        load_dotenv()
        self.ya_disk_token = ya_disk_token
        self.vk_token = os.getenv('VK_API_TOKEN')

    def upload_photos(self, user_id: int) -> bool:
        api_vk = ApiVK(self.vk_token)
        photos = api_vk.get_url_user_photos(user_id)
        api_ya_disk = ApiYaDisk(self.ya_disk_token)
        return api_ya_disk.upload_photo(photos, f'VKPhoto_user_id_{user_id}')

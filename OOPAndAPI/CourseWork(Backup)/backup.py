from api_vk import ApiVK
from api_ya_disk import ApiYaDisk

class Backup:
    def __init__(self,  ya_disk_token: str) -> None:
        self.ya_disk_token = ya_disk_token

    def upload_photos(self, user_id: int) -> list[dict]:
        api_vk = ApiVK()
        photos = api_vk.get_url_user_photos(user_id)
        api_ya_disk = ApiYaDisk(self.ya_disk_token)
        return api_ya_disk.upload_photo(photos, f'VKPhoto_user_id_{user_id}')

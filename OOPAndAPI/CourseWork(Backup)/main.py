import os
from dotenv import load_dotenv
from pprint import pprint

from api_vk import ApiVK
from api_ya_disk import ApiYaDisk


if __name__ == '__main__':
    load_dotenv()

    vk_token = os.getenv('VK_API_TOKEN')
    ya_disk_token = os.getenv('YA_DISK_API_TOKEN')
    
    api_vk = ApiVK(vk_token)
    photos = api_vk.get_url_user_photos(1)

    api_ya_disk = ApiYaDisk(ya_disk_token)
    res = api_ya_disk.upload_photo(photos, 'VKPhoto')
    print(list(res))

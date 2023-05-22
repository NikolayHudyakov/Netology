import os
from dotenv import load_dotenv
from api_vk import ApiVk
from pprint import pprint


if __name__ == '__main__':
    load_dotenv()

    vk_api_token = os.getenv('VK_API_TOKEN')
    
    api_vk = ApiVk(vk_api_token)
    pprint(api_vk.get_url_user_photos(1))
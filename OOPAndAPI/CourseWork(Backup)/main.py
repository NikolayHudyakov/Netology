import os
from dotenv import load_dotenv
from backup import Backup


if __name__ == '__main__':
    load_dotenv()

    ya_disk_token = os.getenv('YA_DISK_API_TOKEN')
    user_id = 1
    
    backup = Backup(ya_disk_token)
    backup.upload_photos(user_id)
   
    
    

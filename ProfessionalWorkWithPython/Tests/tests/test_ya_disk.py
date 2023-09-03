from unittest import TestCase
from ya_disk import YaDisk
import os
from dotenv import load_dotenv


class TestYaDisk(TestCase):
    def setUp(self) -> None:
        load_dotenv()
        ya_disk_token = os.getenv('YA_DISK_API_TOKEN')
        self.ya_disk = YaDisk(ya_disk_token)

    def test_create_folder(self):
        status_code = self.ya_disk.create_folder('test')
        self.assertEquals(status_code, 200)

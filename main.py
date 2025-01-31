import requests
from pprint import pprint
import requests
from pprint import pprint
import configparser
import tqdm
from vk import VK
from yandex_disk import YandexDisk
import logging

logging.basicConfig( # static function
     level=logging.INFO,
     filename='final_paper.log',
     filemode='a',
    format='[%(asctime)s] %(levelname)s - %(message)s'
 )

logging.info("Test")
logging.debug('Testing')

congig = configparser.ConfigParser()
congig.read('settings.ini')
vk_tk = congig['Tokens']['vk_token']
user_id = congig['Tokens']['user_id']
yandex_token = congig['Tokens']['yd_token']
first_user = VK(vk_tk)
first_user_pics = first_user.photos_get(user_id)
logging.info('Got user pictures from VK')
yandex_object = YandexDisk(yandex_token)
yandex_object.delete_folder()
logging.info('Folder is deleted')
yandex_object.create_folder()
logging.info('Folder is created')
photos = yandex_object.upload_pictures(first_user_pics)
if photos:
    logging.info('Program ended successfully')
else:
    logging.info('Program did not end successfully')





import requests
from pprint import pprint
from show_picture import ShowPicture
import logging


class VK:

    def __init__(self, token, version='5.199'):
        logging.debug('VK object was created')
        self.params = {
            'access_token': token,
            'v': version
        }
        self.base = 'https://api.vk.com/method/'

    def photos_get(self, user_id, count=5):
        logging.info('Pictures are in a gotten from VK profile')
        url = f'{self.base}photos.get'
        params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'rev': 0,
            'extended': 1,
            'photo_sizes': 1,
            'count': count
        }
        params.update(self.params)
        response = requests.get(url, params)

        if response.status_code == 200:
            content = response.json()
            list_of_objects = []
            for photo in content['response']['items']:
                sizes = photo['sizes']
                print(sizes[-1])
                size = sizes[-1]['type']
                url = sizes[-1]['url']
                likes = photo['likes']['count']
                date = photo['date']
                first_object = ShowPicture(url, likes, size, date)  # lets us return different number of parameters
                list_of_objects.append(first_object)
                logging.info('ShowPicture object is created and added to the list of objects')
            return list_of_objects
        else:
            logging.error('Status code is not equal 200')
            return []

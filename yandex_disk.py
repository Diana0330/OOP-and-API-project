import requests
import json
import logging

class YandexDisk:

    def __init__(self, yandex_token):
        self.yandex_token = yandex_token
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.folder_name = 'Final_paper'
        self.headers = {
            'Authorization': f'OAuth {self.yandex_token}',
            'Content-Type': 'application/json'
        }

    def __folder_existence(self):
        url = f'{self.base_url}'
        params = {
            'path': self.folder_name
        }
        response = requests.get(url, params=params, headers=self.headers)
        final_response = response.status_code
        if final_response == 200:
            return True
        else:
            return False

    def create_folder(self): # folder name created
        if self.__folder_existence() == False:
            url = f'{self.base_url}'
            params = {
                'path': self.folder_name
            }
            response = requests.put(url, params=params, headers=self.headers)


    def upload_pictures(self, list_of_pictures):
        url = f'{self.base_url}/upload'
        number_of_likes = []
        for picture in list_of_pictures:
            updated_name = ''
            if picture.likes in number_of_likes:
                updated_name = picture.get_file_name_date()
                logging.info('Picture name is updated, and date is added')
            else:
                updated_name = picture.get_file_name()
                number_of_likes.append(picture.likes)
                logging.info('Picture name kept the same')
            params = {
                'path': f'{self.folder_name}/{updated_name}',
                'url': picture.url,
                'overwrite': 'true'

            }
            response = requests.post(url, params=params, headers=self.headers)
            final_response = response.status_code
            content = response.json()
            print(content)
            if final_response != 202:
                logging.error('Status code is not equal 202')
                return False
            else:
                logging.debug(f'Picture is uploaded successfully')
        YandexDisk.__save_info(list_of_pictures)
        return True

    def delete_folder(self):
        if self.__folder_existence() == True:
            url = f'{self.base_url}'
            params = {
                'path': self.folder_name,
                'force_async': 'false'
            }
            response = requests.delete(url, params=params, headers=self.headers)
            final_response = response.status_code
            if final_response == 202:
                logging.info(f'YandexDisk delete_folder() success {self.folder_name}')
            else:
                logging.error(f'YandexDisk delete_folder() error {self.folder_name}')
            print(final_response)
    @staticmethod
    def __save_info(list_of_objects):
        output_data = [] # list of dictionaries
        number_of_likes = [] # number of likes for a photo
        for picture in list_of_objects:
            updated_name = ''
            if picture.likes in number_of_likes:
                updated_name = picture.get_file_name_date()
                logging.info('Date is added to a picture name')
            else:
                updated_name = picture.get_file_name()
                number_of_likes.append(picture.likes)
                logging.info('Original name kept')
            new_dict = {'file_name': updated_name, 'size': picture.size}
            output_data.append(new_dict)

        with open('pictures.json','w') as file:
            json.dump(output_data, file)




import os
from urllib.parse import urlparse
import datetime
class ShowPicture:  # represents each pic
    def __init__(self, url, likes, size, date):
        self.url = url
        self.likes = likes
        self.size = size
        self.date = date

    def get_file_name(self): # we created file_name
        path = urlparse(self.url).path
        ext = os.path.splitext(path)[1]
        return f'{self.likes}{ext}'

    # add
    def get_file_name_date(self): # data - number of likes.jpg
    # generate filename with regards to the current date
        current_date = self.date
        first_file = self.get_file_name()
        return f'{current_date}-{first_file}'

import requests
import os
import shutil

def get_cats(dest_folder, file_name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    cat_binary = get_binarydata(url)
    store_image(dest_folder, file_name, cat_binary)


def get_binarydata(url):
    response = requests.get(url, stream=True)
    return response.raw


def store_image(dest_folder, file_name, cat_binary):
    new_file = os.path.join(dest_folder, file_name + '.jpg')
    with open(new_file, 'wb') as fout:
        shutil.copyfileobj(cat_binary, fout)



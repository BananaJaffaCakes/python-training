import requests

def get_cats(dest_folder, file_name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    cat_binary = get_binarydata(url)
    store_image(dest_folder, file_name, cat_binary)
    


def get_binarydata(url):
    response = requests.get(url, stream=True)
    return response.raw


def store_image(dest_folder, file_name, cat_binary):
    print(dest_folder)
    print(file_name)
    #print('{}'.format(i), end=',')



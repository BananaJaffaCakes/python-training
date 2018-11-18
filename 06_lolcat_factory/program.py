import os
import cat_service
import subprocess
import platform

def main():
    print_header()
    storage_folder = create_folder()
    download_data(storage_folder)
    open_folder(storage_folder)


def print_header():
    print('------------------------')
    print('     LOLCat Factory')
    print('------------------------')


def create_folder():
    new_folder = 'LOLCats'
    #print(os.path.abspath(os.path.join('.', new_folder)))

    #Return directory where current python file is stored
    folder_path = os.path.dirname(__file__)
    full_folder_path = os.path.join(folder_path, new_folder)
    
    if not os.path.exists(full_folder_path) or not os.path.isdir(full_folder_path):
        print('Create folder: Creating at {}'.format(full_folder_path))
        os.mkdir(full_folder_path)
    else:
        print('Create folder: Already exists, skipping.')

    return full_folder_path


def download_data(dest_folder):
    for i in range(1,9):
        print('Download {} started...'.format(i), end=' ')
        file_name = 'lolcat_{}'.format(i)
        cat_service.get_cats(dest_folder, file_name)
        print('completed')
    print('All Downloads complete!')


def open_folder(folder):
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('OS not supported: {}'.format(platform.system()))


if(__name__ == '__main__'):
    main()


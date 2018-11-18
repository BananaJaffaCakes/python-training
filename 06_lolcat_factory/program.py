import os

def main():
    print_header()
    storage_folder = create_folder()
    
    #download cats
    #save cat to folder


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

if(__name__ == '__main__'):
    main()


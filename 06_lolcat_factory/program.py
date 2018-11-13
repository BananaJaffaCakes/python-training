import os

def main():
    print_header()
    create_folder()
    
    #download cats
    #save cat to folder


def print_header():
    print('------------------------')
    print('     LOLCat Factory')
    print('------------------------')


def create_folder():
    new_folder = 'LOLCats'
    
    print(os.path.abspath(new_folder))


if(__name__ == '__main__'):
    main()


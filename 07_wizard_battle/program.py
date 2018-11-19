def main():
    print_header()
    run_game_loop()


def print_header():
    print('----------------------------')
    print('----------------------------')
    print('----------------------------')


def run_game_loop():

    while True:
        cmd = input('Wizard has 3 options: [l]ook around, [a]ttack, [r]un away!')

        if cmd == 'l':
            print('Wizard looked around...')
        elif cmd == 'a':
            print('Wizard attacked!')
        elif cmd == 'r':
            print('Wizard runs...')
        else:
            print('Wizard exits!')
            break

            
if(__name__ == '__main__'):
    main()

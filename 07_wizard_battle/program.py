from actors import Creature, Wizard

def main():
    print_header()
    run_game_loop()


def print_header():
    print('----------------------------')
    print('-----------WIZARD-----------')
    print('----------------------------')


def run_game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Dragon', 100),
        Creature('Bat', 3),
        Creature('Evil Wizard', 50)
    ]

    wizard = Wizard('Dunder', 75)

    while True:

        for i in creatures:
            print('Creature import: {}'.format(i))

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

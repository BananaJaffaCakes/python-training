def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------')
    print('   JOURNAL APP')
    print('-----------------')


def run_event_loop():
    cmd = input('Journal Options, [L]ist entries, [A]dd entries, E[x]it journal: ')
    cmd = cmd.lower().strip()
    
    if cmd == 'l':
        print('Listing entries...')
    elif cmd == 'a':
        print('Adding entries...')
    elif cmd == 'x':
        print('Exiting journal...')
    else:
        print('Invalid option...')

main()
import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------')
    print('   JOURNAL APP')
    print('-----------------')


def run_event_loop():
    
    j_name = 'Space'
    j_data = journal.load(j_name) #[] # list()
    cmd = 'NoCommand'
    
    while cmd != 'x' and cmd:
        cmd = input('Journal Options, [L]ist entries, [A]dd entry, [D]elete entry, E[x]it journal: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(j_data)
        elif cmd == 'a':
            add_entries(j_data)
        elif cmd == 'd':
            delete_entries(j_data)            
        elif cmd != 'x' and cmd:
            print("Invalid option '{}'".format(cmd))

    journal.save(j_data, j_name)
    print('Exiting journal...')


def list_entries(j_entries):
    reversed_entries = reversed(j_entries)
    print('<journal entries start>')
    for (index, entry) in enumerate(reversed_entries):
        print('[{}] {}'.format(index+1, entry))
    print('<journal entries end>')


def add_entries(j_entries):
    new_entry = input('Journal entry, <enter> to commit: ')
    journal.add_entry(j_entries, new_entry)


def delete_entries(j_entries):
    entry_position = int(input('Entry number to delete: '))
    journal.delete_entry(j_entries, entry_position)


if(__name__ == '__main__'):
    main()


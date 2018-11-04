import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------')
    print('   JOURNAL APP')
    print('-----------------')


def run_event_loop():
    
    j_name = 'Deep Space'
    j_data = journal.load(j_name) #[] # list()
    cmd = None
    
    while cmd != 'x':
        cmd = input('Journal Options, [L]ist entries, [A]dd entries, E[x]it journal: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(j_data)
        elif cmd == 'a':
            add_entries(j_data)
        elif cmd != 'x':
            print("Invalid option '{}'".format(cmd))

    print('Saving journal...')
    journal.save(j_data)
    print('Exiting journal...')


def list_entries(journal):
    reversed_entries = reversed(journal)
    print('<journal entries start>')
    for (index, entry) in enumerate(reversed_entries):
        print('[{}] {}'.format(index+1, entry))
    print('<journal entries end>')


def add_entries(journal):
    new_entry = input('Journal entry, <enter> to commit: ')
    journal.add_entry(journal, new_entry)


main()
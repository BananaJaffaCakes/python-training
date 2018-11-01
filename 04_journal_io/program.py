def main():
    print_header()
    run_event_loop()
    print('Exiting journal...')


def print_header():
    print('-----------------')
    print('   JOURNAL APP')
    print('-----------------')


def run_event_loop():
    cmd = input('Journal Options, [L]ist entries, [A]dd entries, E[x]it journal: ')
    cmd = cmd.lower().strip()
    
    j_entries = []

    if cmd == 'l':
        list_entries(j_entries)
    elif cmd == 'a':
        add_entries(j_entries)
    elif cmd != 'x':
        print('Invalid option...')


def list_entries(entries):

    for (index, entry) in enumerate(entries):
        print('[{}] {}'.format(index, entry))

def add_entries(entries):
    new_entry = input('Journal entry, <enter> to commit: ')
    updated_entries = entries.append(new_entry)

    return updated_entries



main()
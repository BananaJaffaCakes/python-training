def main():
    print_header()
    run_event_loop()
    print('Exiting journal...')


def print_header():
    print('-----------------')
    print('   JOURNAL APP')
    print('-----------------')


def run_event_loop():
    
    j_entries = []
    cmd = None
    
    while cmd != 'x':
        cmd = input('Journal Options, [L]ist entries, [A]dd entries, E[x]it journal: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(j_entries)
        elif cmd == 'a':
            add_entries(j_entries)
        elif cmd != 'x':
            print("Invalid option '{}'".format(cmd))


def list_entries(entries):
    reversed_entries = reversed(entries)
    print('<journal entries start>')
    for (index, entry) in enumerate(reversed_entries):
        print('[{}] {}'.format(index, entry))
    print('<journal entries end>')

def add_entries(entries):
    new_entry = input('Journal entry, <enter> to commit: ')
    updated_entries = entries.append(new_entry)

    return updated_entries



main()
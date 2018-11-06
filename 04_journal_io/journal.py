import os

def load(name):
    #initialize list
    journal = []

    print('Loading {}...'.format(name))

    #create absolute path to file
    jrl_path = os.path.abspath(
        os.path.join('./04_journal_io/jrl_files/' + name + '.jrl'))
    print('File load location: {}'.format(jrl_path))

    #open file and read each item to to list
    with open(jrl_path) as j_load:
        entries = j_load.readlines()
        for line in entries:
            journal.append(line.rstrip())

    return journal


def save(journal, name):
    print('Saving journal...')

    #create absolute path to new file
    jrl_path = os.path.abspath(
        os.path.join('./04_journal_io/jrl_files/' + name + '.jrl'))
    print('File save location: {}'.format(jrl_path))

    #take entry and write each item to new line
    with open(jrl_path, 'w') as j_save:
        for entry in journal:
            j_save.write(entry + '\n')   


def add_entry(journal, new_entry):
    updated_journal = journal.append(new_entry)
    return updated_journal


